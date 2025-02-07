"""
Repository class for handling student-related database operations.
Implements the base repository interface for managing student records and their academic information.
"""

from sqlalchemy import select, update, func
from backend.domain.filters.student import StudentFilterSet , StudentFilterSchema, StudentChangeRequest
from backend.domain.schemas.student import StudentCreateModel, StudentModel
from backend.domain.models.tables import StudentTable, StudentNoteTable, TeacherTable, CourseTable, SubjectTable, teacher_subject_table
from backend.application.utils.auth import get_password_hash, get_password
from .base import IRepository


class StudentRepository(IRepository[StudentCreateModel,StudentModel, StudentChangeRequest,StudentFilterSchema]):
    """
    Repository for managing students in the database.
    Extends IRepository with specific implementations for student operations.
    """
    def __init__(self, session):
        """Initialize repository with database session."""
        super().__init__(session)

    def create(self, entity: StudentCreateModel) -> StudentTable:
        """
        Create a new student record with hashed password.
        Args:
            entity: StudentCreateModel containing student details
        Returns:
            Created StudentTable instance
        """
        student_dict = entity.model_dump(exclude={'password'})
        hashed_password = get_password_hash(get_password(entity))
        new_student = StudentTable(**student_dict, hashed_password=hashed_password)
        self.session.add(new_student)
        self.session.commit()
        return new_student
    
    def delete(self, entity: StudentModel) -> None:
        """Delete a student from the database."""
        self.session.delete(entity)        
        self.session.commit()

    def update(self, changes: StudentChangeRequest, entity: StudentModel) -> StudentModel:
        """
        Update a student's information.
        Args:
            changes: StudentChangeRequest containing fields to update
            entity: Current StudentModel to be updated
        Returns:
            Updated StudentModel instance
        """
    
        table_entity = self.get_by_id(id=entity.id)
        for key, value in changes.model_dump(exclude_unset=True, exclude_none=True).items():
            setattr(table_entity, key, value)
        self.session.commit()

        return entity
    
    def get_by_id(self, id: str) -> StudentTable:
        """Retrieve a student by their ID."""
        query = self.session.query(StudentTable).filter(StudentTable.entity_id == id)
        result = query.scalar()
        return result
    
    def get(self, filter_params: StudentFilterSchema) -> list[StudentTable]:
        """Get students based on filter parameters."""
        query = select(StudentTable)
        filter_set = StudentFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return self.session.execute(query).scalars().all()
    
    def get_student_by_email(self, email: str) -> StudentTable:
        """
        Retrieve a student by their email address.
        Args:
            email: Email address of the student
        Returns:
            Matching StudentTable instance or None
        """
        query = self.session.query(StudentTable).filter(StudentTable.email == email)
        result = query.first()
        return result
        
    def get_academic_information(self, student_id: str):
        """
        Get academic performance information for a specific student.
        Args:
            student_id: ID of the student
        Returns:
            List of tuples containing student ID, subject ID, and average performance
        """
        query = select(StudentTable.id, StudentNoteTable.subject_id, 
                      (func.sum(StudentNoteTable.note_value)/func.count()).label("academic_performance"))
        query = query.join(StudentNoteTable, StudentTable.id == StudentNoteTable.student_id)
        query = query.where(StudentTable.id == student_id)
        query = query.group_by(StudentTable.id, StudentNoteTable.subject_id)
        result = self.session.execute(query).all()
        return result
    
    def get_students_by_teacher(self, teacher_id: str):
        """
        Get all students associated with a specific teacher through subjects and courses.
        Args:
            teacher_id: ID of the teacher
        Returns:
            List of tuples containing teacher, subject, course, and student information
        """
        query = select(TeacherTable.id, SubjectTable, CourseTable, StudentTable)
        query = query.join(teacher_subject_table, TeacherTable.id == teacher_subject_table.c.teacher_id)
        query = query.join(SubjectTable, teacher_subject_table.c.subject_id == SubjectTable.entity_id)
        query = query.join(CourseTable, SubjectTable.course_id == CourseTable.entity_id)
        query = query.join(StudentTable, CourseTable.entity_id == StudentTable.course_id)
        query = query.where(TeacherTable.id == teacher_id)
        query = query.distinct(StudentTable.id)
        return self.session.execute(query).all()

    
        

