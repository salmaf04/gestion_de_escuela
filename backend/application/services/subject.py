from sqlalchemy.orm import Session
from sqlalchemy import select, update
from backend.domain.filters.subject import SubjectFilterSet , SubjectFilterSchema, SubjectChangeRequest
from backend.domain.schemas.subject import SubjectCreateModel, SubjectModel
from backend.domain.models.tables import SubjectTable
import uuid
from backend.application.services.classroom import ClassroomPaginationService
from backend.application.services.course import CoursePaginationService
from backend.infrastructure.repositories.subject import SubjectRepository

"""
This module defines services for creating, retrieving, updating, and deleting subject records.

Classes:
    SubjectCreateService: A service for creating new subject records.
    SubjectDeletionService: A service for deleting subject records.
    SubjectUpdateService: A service for updating subject records.
    SubjectPaginationService: A service for retrieving subject records based on various criteria.

Classes Details:

1. SubjectCreateService:
    - This service is responsible for creating new subject records.
    - It utilizes the SubjectRepository to interact with the database.
    - It also uses ClassroomPaginationService and CoursePaginationService to retrieve classroom and course details.
    
    Methods:
        - __init__(session): Initializes the service with a database session and sets up necessary service instances.
        - create_subject(subject: SubjectCreateModel) -> SubjectTable: 
            Creates a new subject record using the provided SubjectCreateModel and returns the created SubjectTable object.

2. SubjectDeletionService:
    - This service is responsible for deleting subject records.
    - It uses the SubjectRepository to perform deletion operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - delete_subject(subject: SubjectModel) -> None: 
            Deletes the specified subject record.

3. SubjectUpdateService:
    - This service is responsible for updating subject records.
    - It uses the SubjectRepository to perform update operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - update_one(changes: SubjectChangeRequest, subject: SubjectModel) -> SubjectModel: 
            Updates the specified subject record with the provided changes and returns the updated SubjectModel.

4. SubjectPaginationService:
    - This service is responsible for retrieving subject records based on different criteria.
    - It uses the SubjectRepository to fetch data from the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - get_subject_by_id(id: uuid.UUID) -> SubjectTable: 
            Retrieves a subject record by the specified ID.
        - get_subjects(filter_params: SubjectFilterSchema) -> list[SubjectTable]: 
            Retrieves a list of subjects based on the provided filter parameters.
        - get_subjects_by_students(student_id: str): 
            Retrieves subjects associated with a specific student.
        - get_subjects_by_teacher(teacher_id: str): 
            Retrieves subjects taught by a specific teacher.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - SubjectRepository for database operations related to subjects.
    - SubjectCreateModel, SubjectModel, SubjectTable, and other domain models for data representation.
    - SubjectFilterSchema and SubjectFilterSet for filtering subject records.
    - UUID for handling unique identifiers.
    - ClassroomPaginationService and CoursePaginationService for retrieving related information.
"""
class SubjectCreateService :
    def __init__(self, session):
        self.repo_instance = SubjectRepository(session)
        self.classroom_pagination_service = ClassroomPaginationService(session)
        self.course_pagination_service = CoursePaginationService(session)

    def create_subject(self, subject:SubjectCreateModel) -> SubjectTable :
        classroom = self.classroom_pagination_service.get_classroom_by_id(id=subject.classroom_id)
        course = self.course_pagination_service.get_course_by_id(id=subject.course_id)
        return self.repo_instance.create(subject, classroom, course)
    
class SubjectDeletionService:
    def __init__(self, session):
        self.repo_instance = SubjectRepository(session)

    def delete_subject(self, subject: SubjectModel) -> None :
        return self.repo_instance.delete(subject)
        
class SubjectUpdateService :
    def __init__(self, session):
        self.repo_instance = SubjectRepository(session)

    def update_one(self, changes : SubjectChangeRequest , subject : SubjectModel ) -> SubjectModel: 
        return self.repo_instance.update(changes, subject)

class SubjectPaginationService :
    def __init__(self, session):
        self.repo_instance = SubjectRepository(session)
    
    def get_subject_by_id(self, id:uuid.UUID ) -> SubjectTable :
        return self.repo_instance.get_by_id(id)
    
    def get_subjects(self, filter_params: SubjectFilterSchema) -> list[SubjectTable] :
        return self.repo_instance.get(filter_params)
    
    def get_subjects_by_students(self, student_id: str) :
        return self.repo_instance.get_subjects_by_students(student_id=student_id)
    
    def get_subjects_by_teacher(self, teacher_id: str) :
        return self.repo_instance.get_subjects_by_teacher(teacher_id=teacher_id)
    