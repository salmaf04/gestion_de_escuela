from sqlalchemy import select, update
from backend.domain.filters.subject import SubjectFilterSet , SubjectFilterSchema, SubjectChangeRequest
from backend.domain.schemas.subject import SubjectCreateModel, SubjectModel
from backend.domain.models.tables import SubjectTable, CourseTable, StudentTable, teacher_subject_table, ClassroomTable
import uuid
from backend.application.services.classroom import ClassroomPaginationService
from backend.application.services.course import CoursePaginationService
from .base import IRepository

"""
Repository class for handling subject-related database operations.
Implements the base repository interface for managing academic subjects and their relationships.
"""

class SubjectRepository(IRepository[SubjectCreateModel,SubjectTable, SubjectChangeRequest,SubjectFilterSchema]):
    """
    Repository for managing subjects in the database.
    Extends IRepository with specific implementations for subject operations.
    """
    def __init__(self, session):
        """Initialize repository with database session."""
        super().__init__(session)

    def create(self, entity: SubjectCreateModel, classroom, course) -> SubjectTable:
        """
        Create a new subject record and associate it with a classroom.
        Args:
            entity: SubjectCreateModel containing subject details
            classroom: Classroom instance to associate with the subject
            course: Course instance to associate with the subject
        Returns:
            Created SubjectTable instance
        """
        subject_dict = entity.model_dump()
        new_subject = SubjectTable(**subject_dict)
        new_subject.classroom = classroom
        classroom.subjects.append(new_subject)
        self.session.add(new_subject)
        self.session.commit()
        
        subject = self.get(
            filter_params=SubjectFilterSchema(id=new_subject.entity_id)
        )

        return subject

    def delete(self, entity: SubjectTable) -> None:
        """Delete a subject from the database."""
        self.session.delete(entity)
        self.session.commit()

    def update(self, changes: SubjectChangeRequest, entity: SubjectTable) -> SubjectTable:
        """
        Update a subject's information.
        Args:
            changes: SubjectChangeRequest containing fields to update
            entity: Current SubjectTable to be updated
        Returns:
            Updated SubjectTable instance
        """
        query = update(SubjectTable).where(SubjectTable.entity_id == entity.entity_id)
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        self.session.execute(query)
        self.session.commit()
        
        subject = self.get(
            filter_params=SubjectFilterSchema(id=entity.entity_id)
        )

        return subject
           
    def get_by_id(self, id: str) -> SubjectTable:
        """
        Retrieve a subject by its ID.
        Args:
            id: String identifier of the subject
        Returns:
            Matching SubjectTable instance or None
        """
        query = self.session.query(SubjectTable).filter(SubjectTable.entity_id == id)
        result = query.scalar()
        return result
    
    def get(self, filter_params: SubjectFilterSchema) -> list[SubjectTable]:
        """
        Get subjects based on filter parameters.
        Args:
            filter_params: Filter criteria for subjects
        Returns:
            List of matching SubjectTable instances
        """
        query = select(SubjectTable, ClassroomTable, CourseTable)
        query = query.join(ClassroomTable, ClassroomTable.entity_id == SubjectTable.classroom_id)
        query = query.join(CourseTable, CourseTable.entity_id == SubjectTable.course_id)
        filter_set = SubjectFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return self.session.execute(query).all()

    def get_subjects_by_students(self, student_id: str):
        """
        Get all subjects associated with a specific student through their course.
        Args:
            student_id: ID of the student
        Returns:
            List of tuples containing subject, course, and student information
        """
        query = select(SubjectTable, CourseTable, StudentTable, ClassroomTable)
        query = query.join(SubjectTable, CourseTable.entity_id == SubjectTable.course_id)
        query = query.join(StudentTable, CourseTable.entity_id == StudentTable.course_id)
        query = query.where(StudentTable.id == student_id)
        query = query.distinct(SubjectTable.entity_id)
        return self.session.execute(query).all()
    
    def get_subjects_by_teacher(self, teacher_id: str):
        """
        Get all subjects taught by a specific teacher.
        Args:
            teacher_id: ID of the teacher
        Returns:
            List of tuples containing subject and teacher-subject association information
        """
        query = select(SubjectTable, teacher_subject_table)
        query = query.join(teacher_subject_table, SubjectTable.entity_id == teacher_subject_table.c.subject_id)
        query = query.where(teacher_subject_table.c.teacher_id == teacher_id)
        query = query.distinct(SubjectTable.entity_id)
        return self.session.execute(query).all()