from sqlalchemy.orm import Session
from sqlalchemy import select, func, update
from backend.domain.schemas.absence import AbsenceCreateModel
from backend.domain.models.tables import AbsenceTable, StudentTable, SubjectTable, TeacherTable, CourseTable, teacher_subject_table
from backend.application.services.student import StudentPaginationService
from backend.application.services.course import CoursePaginationService
from backend.application.services.subject import SubjectPaginationService
from backend.domain.filters.absence import AbsenceFilterSchema, AbsenceFilterSet, AbsenceChangeRequest
from datetime import datetime
from .base import IRepository
import uuid

"""
Repository class for handling absence-related database operations.
Implements the base repository interface for absence management.
"""

class AbsenceRepository(IRepository[AbsenceCreateModel,AbsenceTable, None,AbsenceFilterSchema]):
    """
    Repository for managing student absences in the database.
    Extends IRepository with specific implementations for absence operations.
    """
    def __init__(self, session):
        """Initialize repository with database session."""
        super().__init__(session)

    def create(self, entity: AbsenceCreateModel) -> AbsenceTable:
        """
        Create a new absence record in the database.
        Args:
            entity: AbsenceCreateModel containing absence details
        Returns:
            Created AbsenceTable instance
        """
        absence_dict = entity.model_dump(exclude={'date'})
        date = datetime.strptime(entity.date, "%d-%m-%Y")
        new_absence = AbsenceTable(**absence_dict, date=date)

        self.session.add(new_absence)
        self.session.commit()
        return new_absence
    
    def get(self, filter_params: AbsenceFilterSchema) -> list[AbsenceTable]:
        """
        Retrieve absences based on filter parameters.
        Args:
            filter_params: Filter criteria for absences
        Returns:
            List of matching AbsenceTable instances
        """
        
        query = select(AbsenceTable.student_id, AbsenceTable.subject_id, func.count().label("absences_by_subject"))
        query = query.group_by(AbsenceTable.subject_id, AbsenceTable.student_id)
        query = query.order_by(AbsenceTable.student_id, AbsenceTable.subject_id)
        total = self.session.execute(query).all()

        final_query = select(AbsenceTable, StudentTable, SubjectTable, CourseTable)
        final_query = final_query.join(StudentTable, AbsenceTable.student_id == StudentTable.entity_id)
        final_query = final_query.join(SubjectTable, AbsenceTable.subject_id == SubjectTable.entity_id) 
        final_query = final_query.join(CourseTable, StudentTable.course_id == CourseTable.entity_id)
        final_query = final_query.order_by(StudentTable.entity_id, SubjectTable.entity_id)
        return self.session.execute(final_query).all(), total
    
    def get_by_id(self, id: str) -> AbsenceTable:
        absence = self.session.query(AbsenceTable).filter(AbsenceTable.entity_id == id)
        return absence.scalar()
    
    def delete(self, entity: AbsenceTable) -> None:
        self.session.delete(entity)
        self.session.commit()

    def update(self, changes: AbsenceChangeRequest, entity: AbsenceTable) -> AbsenceTable:
        update_statement = update(AbsenceTable).where(AbsenceTable.entity_id == entity.entity_id)
        update_statement = update_statement.values(date=changes.date)
        self.session.execute(update_statement)
        self.session.commit()
        return self.get_by_id(id=entity.entity_id)
        
    def get_absence_by_student(self, student_id: uuid.UUID) -> list[AbsenceTable]:
        """
        Get absence statistics for a specific student.
        Args:
            student_id: UUID of the student
        Returns:
            List of absences grouped by subject with count
        """
        query = select(AbsenceTable.student_id, AbsenceTable.subject_id, func.count().label("absences_by_subject"))
        query = query.where(AbsenceTable.student_id == student_id)
        query = query.group_by(AbsenceTable.subject_id, AbsenceTable.student_id)
        query = query.order_by(AbsenceTable.subject_id)
        total = self.session.execute(query).all()
        
        final_query = select(AbsenceTable, StudentTable, SubjectTable, CourseTable)
        final_query = final_query.join(StudentTable, AbsenceTable.student_id == StudentTable.entity_id)
        final_query = final_query.join(SubjectTable, AbsenceTable.subject_id == SubjectTable.entity_id) 
        final_query = final_query.join(CourseTable, StudentTable.course_id == CourseTable.entity_id)
        final_query = final_query.where(AbsenceTable.student_id == student_id)
        final_query = final_query.order_by(SubjectTable.entity_id)
        
        return self.session.execute(final_query).all(), total
    
    def get_absence_by_student_by_teacher(self, teacher_id: uuid.UUID) -> list[AbsenceTable]:
        """
        Get absence statistics for all students under a specific teacher.
        Args:
            teacher_id: UUID of the teacher
        Returns:
            List of absences grouped by student and subject with count

        """
        
        query = select(AbsenceTable.student_id, AbsenceTable.subject_id, func.count().label("absences_by_subject"))
        query = query.where(
            AbsenceTable.subject_id.in_(
                select(teacher_subject_table.c.subject_id).where(teacher_subject_table.c.teacher_id == teacher_id)
            ))
        query = query.group_by(AbsenceTable.subject_id, AbsenceTable.student_id)
        query = query.order_by(AbsenceTable.student_id, AbsenceTable.subject_id)
        total = self.session.execute(query).all()

        final_query = select(AbsenceTable, StudentTable, SubjectTable, CourseTable)
        final_query = final_query.join(StudentTable, AbsenceTable.student_id == StudentTable.entity_id)
        final_query = final_query.join(SubjectTable, AbsenceTable.subject_id == SubjectTable.entity_id) 
        final_query = final_query.join(CourseTable, StudentTable.course_id == CourseTable.entity_id)
        final_query = final_query.where(
            AbsenceTable.subject_id.in_(
                select(teacher_subject_table.c.subject_id).where(teacher_subject_table.c.teacher_id == teacher_id)
            ))
        final_query = final_query.order_by(AbsenceTable.student_id, AbsenceTable.subject_id)
        return self.session.execute(final_query).all(), total

    def get_students_by_teacher(self, teacher_id: uuid.UUID) -> list[StudentTable]:
        """
        Get all students associated with a specific teacher through their courses and subjects.
        Args:
            teacher_id: UUID of the teacher
        Returns:
            List of student IDs
        """
        query = (
            select(StudentTable.id)
            .join(CourseTable, StudentTable.course_id == CourseTable.entity_id)
            .join(SubjectTable, CourseTable.entity_id == SubjectTable.course_id)
            .join(teacher_subject_table, SubjectTable.entity_id == teacher_subject_table.c.subject_id)
            .join(TeacherTable, teacher_subject_table.c.teacher_id == TeacherTable.id)
            .where(TeacherTable.id == teacher_id)
            .distinct()
            .subquery()
        )
        return query