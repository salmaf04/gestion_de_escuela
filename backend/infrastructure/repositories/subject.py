from sqlalchemy import select, update
from backend.domain.filters.subject import SubjectFilterSet , SubjectFilterSchema, SubjectChangeRequest
from backend.domain.schemas.subject import SubjectCreateModel, SubjectModel
from backend.domain.models.tables import SubjectTable, CourseTable, StudentTable, teacher_subject_table
import uuid
from backend.application.services.classroom import ClassroomPaginationService
from backend.application.services.course import CoursePaginationService
from .base import IRepository

class SubjectRepository(IRepository[SubjectCreateModel,SubjectTable, SubjectChangeRequest,SubjectFilterSchema]):
    def __init__(self, session):
        super().__init__(session)

    def create(self, entity: SubjectCreateModel, classroom, course) -> SubjectTable :
        subject_dict = entity.model_dump()
        new_subject = SubjectTable(**subject_dict)
        new_subject.classroom = classroom
        classroom.subjects.append(new_subject)
        self.session.add(new_subject)
        self.session.commit()
        return new_subject

    def delete(self, entity: SubjectTable) -> None :
        self.session.delete(entity)
        self.session.commit()

    def update(self, changes : SubjectChangeRequest , entity : SubjectTable) -> SubjectTable :
        query = update(SubjectTable).where(SubjectTable.entity_id == entity.entity_id)
 
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        self.session.execute(query)
        self.session.commit()
        
        subject = entity.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return subject
           
    def get_by_id(self, id: str ) -> SubjectTable :
        query = self.session.query(SubjectTable).filter(SubjectTable.entity_id == id)

        result = query.scalar()

        return result
    
    def get(self, filter_params: SubjectFilterSchema) -> list[SubjectTable] :
        query = select(SubjectTable)
        filter_set = SubjectFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return self.session.execute(query).scalars().all()

    def get_subjects_by_students(self, student_id: str) :
        query = select(SubjectTable, CourseTable, StudentTable)
        query = query.join(SubjectTable, CourseTable.entity_id == SubjectTable.course_id)
        query = query.join(StudentTable, CourseTable.entity_id == StudentTable.course_id)
        query = query.where(StudentTable.id == student_id)
        query = query.distinct(SubjectTable.entity_id)
        return self.session.execute(query).all()
    
    def get_subjects_by_teacher(self, teacher_id: str) :
        query = select(SubjectTable, teacher_subject_table)
        query = query.join(teacher_subject_table, SubjectTable.entity_id == teacher_subject_table.c.subject_id)
        query = query.where(teacher_subject_table.c.teacher_id == teacher_id)
        query = query.distinct(SubjectTable.entity_id)
        return self.session.execute(query).all()