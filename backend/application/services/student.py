from sqlalchemy.orm import Session
from sqlalchemy import select, update, func
from backend.domain.filters.student import StudentFilterSet , StudentFilterSchema, StudentChangeRequest
from backend.domain.schemas.student import StudentCreateModel, StudentModel
from backend.domain.models.tables import StudentTable, StudentNoteTable, TeacherTable, CourseTable, SubjectTable, teacher_subject_table
from backend.application.services.course import CoursePaginationService
from ..utils.auth import get_password_hash, get_password
from ..utils.note_average import  calculate_student_average
import uuid
from backend.infrastructure.repositories.student import StudentRepository

"""
This module defines services for creating, retrieving, updating, and deleting student records, as well as updating student note averages.

Classes:
    StudentCreateService: A service for creating new student records.
    StudentDeletionService: A service for deleting student records.
    StudentUpdateService: A service for updating student records.
    StudentPaginationService: A service for retrieving student records based on various criteria.
    UpdateNoteAverageService: A service for updating the average note of a student.

Classes Details:

1. StudentCreateService:
    - This service is responsible for creating new student records.
    - It utilizes the StudentRepository to interact with the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - create_student(student: StudentCreateModel) -> StudentTable: 
            Creates a new student record using the provided StudentCreateModel and returns the created StudentTable object.

2. StudentDeletionService:
    - This service is responsible for deleting student records.
    - It uses the StudentRepository to perform deletion operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - delete_student(student: StudentModel) -> None: 
            Deletes the specified student record.

3. StudentUpdateService:
    - This service is responsible for updating student records.
    - It uses the StudentRepository to perform update operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - update_one(changes: StudentChangeRequest, student: StudentModel) -> StudentModel: 
            Updates the specified student record with the provided changes and returns the updated StudentModel.

4. StudentPaginationService:
    - This service is responsible for retrieving student records based on different criteria.
    - It uses the StudentRepository to fetch data from the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - get_student_by_email(email: str) -> StudentTable: 
            Retrieves a student record by the specified email.
        - get_student_by_id(id: uuid.UUID) -> StudentTable: 
            Retrieves a student record by the specified ID.
        - get_students(filter_params: StudentFilterSchema) -> list[StudentTable]: 
            Retrieves a list of students based on the provided filter parameters.
        - get_academic_information(student_id: str): 
            Retrieves academic information for a specific student.
        - get_students_by_teacher(teacher_id: str): 
            Retrieves students taught by a specific teacher.

5. UpdateNoteAverageService:
    - This service is responsible for updating the average note of a student.
    
    Methods:
        - update_note_average(session: Session, student_id: str, new_note: int): 
            Updates the average note for a student based on a new note and commits the change to the database.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - StudentRepository for database operations related to students.
    - StudentCreateModel, StudentModel, StudentTable, and other domain models for data representation.
    - StudentFilterSchema and StudentFilterSet for filtering student records.
    - UUID for handling unique identifiers.
    - Utility functions for password hashing and note average calculation.
"""

class StudentCreateService :
    def __init__(self, session):
        self.repo_instance = StudentRepository(session)

    def create_student(self, student:StudentCreateModel) -> StudentTable :
        return self.repo_instance.create(student)
   
class StudentDeletionService:
    def __init__(self, session):
        self.repo_instance = StudentRepository(session)

    def delete_student(self, student: StudentModel) -> None :
        return self.repo_instance.delete(student)
            
class StudentUpdateService :
    def __init__(self, session):
        self.repo_instance = StudentRepository(session)

    def update_one(self, changes : StudentChangeRequest , student : StudentModel ) -> StudentModel: 
        return self.repo_instance.update(changes, student)
        
class StudentPaginationService :
    def __init__(self, session):
        self.repo_instance = StudentRepository(session)

    def get_student_by_email(self, email: str) -> StudentTable :
        self.repo_instance.get_student_by_email(email)
       
    def get_student_by_id(self, id:uuid.UUID ) -> StudentTable :
        return self.repo_instance.get_by_id(id)
        
    def get_students(self, filter_params: StudentFilterSchema) -> list[StudentTable] :
        return self.repo_instance.get(filter_params)
    
    def get_academic_information(self, student_id: str) :
        return self.repo_instance.get_academic_information(student_id)
        
    def get_students_by_teacher(self, teacher_id: str) :
        return self.repo_instance.get_students_by_teacher(teacher_id)
    
class UpdateNoteAverageService : 
    def update_note_average(self, session: Session, student_id: str, new_note : int ) : 
        new_avergage = calculate_student_average(session=session, student_id=student_id, new_note=new_note)
        query = update(StudentTable).where(StudentTable.id == student_id).values(average_note=new_avergage)
        session.execute(query)
        session.commit()