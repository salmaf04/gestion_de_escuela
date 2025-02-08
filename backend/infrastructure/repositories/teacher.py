from sqlalchemy import func, asc, distinct
from backend.application.serializers.teacher import TeacherMapper
from backend.domain.schemas.teacher import TeacherCreateModel, TeacherModel
from backend.domain.models.tables import TeacherTable, teacher_subject_table, TeacherNoteTable, UserTable, SanctionTable, StudentTable, SubjectTable, CourseTable
from sqlalchemy import and_, update
import uuid
from sqlalchemy import select
from backend.domain.filters.teacher import TeacherFilterSet , TeacherFilterSchema, TeacherChangeRequest
from backend.domain.filters.subject import SubjectFilterSchema
from backend.application.utils.auth import get_password_hash, get_password
from backend.application.services.subject import SubjectPaginationService
from sqlalchemy import func
from backend.application.utils.valoration_average import get_teacher_valoration_average, calculate_teacher_average
from backend.domain.models.tables import ClassroomTable, TechnologicalMeanTable, SubjectTable, teacher_subject_table
from sqlalchemy.orm import aliased
from fastapi import HTTPException, status
from .base import IRepository


class TeacherRepository(IRepository[TeacherCreateModel,TeacherModel, TeacherChangeRequest,TeacherFilterSchema]):
    """
    Repository for managing teachers in the database.
    Extends IRepository with specific implementations for teacher operations.
    """
    def __init__(self, session):
        """Initialize repository with database session."""
        super().__init__(session)

    def create(self, entity: TeacherCreateModel, subjects: SubjectTable) -> TeacherTable:
        """
        Create a new teacher record with subject associations and hashed password.
        Args:
            entity: TeacherCreateModel containing teacher details
            subjects: List of SubjectTable instances to associate with teacher
        Returns:
            Created TeacherTable instance
        """
        teacher_dict = entity.model_dump(exclude={'password', 'subjects'})
        hashed_password = get_password_hash(get_password(entity))
        new_teacher = TeacherTable(**teacher_dict, hashed_password=hashed_password)
        new_teacher.teacher_subject_association = subjects if subjects else []
        self.session.add(new_teacher)
        self.session.commit()
        return new_teacher

    def delete(self, entity: TeacherModel) -> None:
        """Delete a teacher from the database."""
        self.session.delete(entity)
        self.session.commit()

    def update(self, changes: TeacherChangeRequest, entity: TeacherModel, subjects=None) -> TeacherModel:
        """Update a teacher's information."""
    
        table_entity = self.get_by_id(id=entity.id)
        
        if subjects :
            table_entity.teacher_subject_association = subjects
        
        for key, value in changes.items() :
            setattr(table_entity, key, value)
        self.session.commit()

        return entity

    def get_by_id(self, id: str) -> TeacherTable:
        """Retrieve a teacher by their ID."""
        query = self.session.query(TeacherTable).filter(TeacherTable.entity_id == id)
        result = query.scalar()
        return result
    
    def get(self, filter_params: TeacherFilterSchema) -> list[TeacherTable] :
        query = select(TeacherTable)
        filter_set = TeacherFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        teachers = self.session.scalars(query).all()
        return teachers
            
    def get_teacher_by_email(self, email: str) -> TeacherTable :
        query = self.session.query(TeacherTable).filter(TeacherTable.email == email)
        result = query.first()
        return result

    def get_teachers_average_better_than_8(self) -> tuple[list, list]:
        """Get teachers with average valoration better than 8 and their subjects."""
        subjects = []
        query = select(TeacherTable.name, TeacherTable.id, TeacherTable.average_valoration).where(TeacherTable.average_valoration > 8)
        results = self.session.execute(query).all()
        mapper = TeacherMapper()

        for teacher in results:
            teacher = self.get_by_id(id=teacher.id)
            subjects.append(mapper.to_subject_list(teacher.teacher_subject_association))
        return results, subjects

    def get_teachers_by_technological_classroom(self):
        """Get teachers associated with technological classrooms."""
        query = select(TeacherTable, SubjectTable, ClassroomTable, TechnologicalMeanTable.name, TechnologicalMeanTable.state)   
        query = query.join(teacher_subject_table, TeacherTable.id == teacher_subject_table.c.teacher_id)
        query = query.join(SubjectTable, teacher_subject_table.c.subject_id == SubjectTable.entity_id)
        query = query.join(ClassroomTable, SubjectTable.classroom_id == ClassroomTable.entity_id)
        query = query.join(TechnologicalMeanTable, ClassroomTable.entity_id == TechnologicalMeanTable.classroom_id)
        query = query.distinct(TechnologicalMeanTable.id,ClassroomTable.entity_id, TeacherTable.id)
        query = query.order_by(asc(TeacherTable.id))
        return self.session.execute(query).all()

    def get_teachers_by_sanctions(self):
        """Get teachers with sanctions and their top 3 grades."""
        latest_sanction_subquery = (
            select(
                SanctionTable.teacher_id,
                func.min(SanctionTable.date).label('latest_sanction_date')
            )
            .group_by(SanctionTable.teacher_id)
            .subquery()
        )
        grade_rank = func.row_number().over(
            partition_by=TeacherTable.id,
            order_by=TeacherNoteTable.grade
        ).label('grade_rank')
        query = select(TeacherTable.id, TeacherTable.name, latest_sanction_subquery.c.latest_sanction_date, TeacherNoteTable.grade)
        query = query.add_columns(grade_rank)
        query = query.join(latest_sanction_subquery, TeacherTable.id == latest_sanction_subquery.c.teacher_id)
        query = query.outerjoin(TeacherNoteTable, TeacherTable.id == TeacherNoteTable.teacher_id)
        query = query.where(TeacherTable.id.in_(select(SanctionTable.teacher_id)))
        query = query.order_by(
            TeacherTable.id,
            TeacherNoteTable.grade,
        )
        subquery = query.subquery()
        final_query = select(subquery).where(subquery.c.grade_rank <= 3)
        return self.session.execute(final_query).all(), self.get_teachers_by_technological_classroom()

    def create_teacher_subject(self, teacher_id: str, subject_id: str):
        """Create a new teacher-subject association."""
        teacher_subject = teacher_subject_table.insert().values(teacher_id=teacher_id, subject_id=subject_id)
        self.session.execute(teacher_subject)
        self.session.commit()

    def get_teacher_subjects(self, id: str) -> list[str]:
        """Get list of subjects for a specific teacher."""
        query = select(TeacherTable).where(TeacherTable.entity_id == id)
        teacher = self.session.execute(query).scalars().first()
        subjects = teacher.teacher_subject_association
        return TeacherMapper().to_subject_list(subjects)

    def get_teachers_by_students(self, student_id: str):
        """Get teachers associated with a specific student through courses."""
        query = select(TeacherTable, SubjectTable, CourseTable, StudentTable)
        query = query.join(teacher_subject_table, TeacherTable.id == teacher_subject_table.c.teacher_id)
        query = query.join(SubjectTable, teacher_subject_table.c.subject_id == SubjectTable.entity_id)
        query = query.join(CourseTable, SubjectTable.course_id == CourseTable.entity_id)
        query = query.join(StudentTable, CourseTable.entity_id == StudentTable.course_id)
        query = query.where(StudentTable.id == student_id)
        query = query.order_by(TeacherTable.id)
        return self.session.execute(query).all()