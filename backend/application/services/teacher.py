from sqlalchemy.orm import Session
from sqlalchemy import func, asc, distinct
from backend.application.serializers.teacher import TeacherMapper
from backend.domain.schemas.teacher import TeacherCreateModel, TeacherModel
from backend.domain.models.tables import TeacherTable, teacher_subject_table, TeacherNoteTable, UserTable, SanctionTable
from sqlalchemy import and_, update
import uuid
from sqlalchemy import select
from backend.domain.filters.teacher import TeacherFilterSet , TeacherFilterSchema, TeacherChangeRequest
from backend.domain.filters.subject import SubjectFilterSchema
from ..utils.auth import get_password_hash, get_password
from backend.application.services.subject import SubjectPaginationService
from sqlalchemy import func
from backend.application.utils.valoration_average import get_teacher_valoration_average, calculate_teacher_average
from backend.domain.models.tables import ClassroomTable, TechnologicalMeanTable, SubjectTable, teacher_subject_table
from sqlalchemy.orm import aliased
from fastapi import HTTPException, status
from backend.infrastructure.repositories.teacher import TeacherRepository

"""
This module defines services for creating, retrieving, updating, and deleting teacher records, as well as managing teacher-subject associations.

Classes:
    TeacherCreateService: A service for creating new teacher records.
    TeacherDeletionService: A service for deleting teacher records.
    TeacherUpdateService: A service for updating teacher records.
    TeacherPaginationService: A service for retrieving teacher records based on various criteria.
    TeacherSubjectService: A service for managing teacher-subject associations.

Classes Details:

1. TeacherCreateService:
    - This service is responsible for creating new teacher records.
    - It utilizes the TeacherRepository to interact with the database.
    - It also uses SubjectPaginationService to retrieve subject details associated with the teacher.
    
    Methods:
        - __init__(session): Initializes the service with a database session and sets up necessary service instances.
        - create_teacher(teacher: TeacherCreateModel) -> TeacherTable: 
            Creates a new teacher record using the provided TeacherCreateModel and returns the created TeacherTable object.

2. TeacherDeletionService:
    - This service is responsible for deleting teacher records.
    - It uses the TeacherRepository to perform deletion operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - delete_teacher(teacher: TeacherModel) -> None: 
            Deletes the specified teacher record.

3. TeacherUpdateService:
    - This service is responsible for updating teacher records.
    - It uses the TeacherRepository to perform update operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - update(changes: TeacherChangeRequest, teacher: TeacherModel) -> TeacherModel: 
            Updates the specified teacher record with the provided changes and returns the updated TeacherModel.

4. TeacherPaginationService:
    - This service is responsible for retrieving teacher records based on different criteria.
    - It uses the TeacherRepository to fetch data from the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - get_teacher_by_email(email: str) -> TeacherTable: 
            Retrieves a teacher record by the specified email.
        - get_teacher_by_id(id: uuid.UUID) -> TeacherTable: 
            Retrieves a teacher record by the specified ID.
        - get_teachers(filter_params: TeacherFilterSchema) -> list[TeacherTable]: 
            Retrieves a list of teachers based on the provided filter parameters.
        - get_teachers_average_better_than_8(): 
            Retrieves teachers with an average rating better than 8.
        - get_teachers_by_technological_classroom(): 
            Retrieves teachers associated with technological classrooms.
        - get_teachers_by_sanctions(): 
            Retrieves teachers with sanctions.
        - get_teachers_by_students(student_id: str): 
            Retrieves teachers associated with a specific student.

5. TeacherSubjectService:
    - This service is responsible for managing teacher-subject associations.
    
    Methods:
        - create_teacher_subject(session: Session, teacher_id: str, subject_id: str): 
            Creates an association between a teacher and a subject.
        - get_teacher_subjects(id: uuid.UUID) -> list[str]: 
            Retrieves the subjects associated with a specific teacher.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - TeacherRepository for database operations related to teachers.
    - TeacherCreateModel, TeacherModel, TeacherTable, and other domain models for data representation.
    - TeacherFilterSchema and TeacherFilterSet for filtering teacher records.
    - UUID for handling unique identifiers.
    - Utility functions for password hashing and valoration average calculation.
    - FastAPI for handling HTTP exceptions.
"""
class TeacherCreateService :
    def __init__ (self, session):
        self.repo_istance = TeacherRepository(session)
        self.subject_pagination = SubjectPaginationService(session)
    
    def create_teacher(self, teacher: TeacherCreateModel) -> TeacherTable :
        subjects = self.subject_pagination.get_subjects(filter_params=SubjectFilterSchema(name=teacher.list_of_subjects)) if teacher.list_of_subjects else None
        return self.repo_istance.create(teacher, subjects=subjects)
class TeacherDeletionService:
    def __init__ (self, session):
        self.repo_istance = TeacherRepository(session)

    def delete_teacher(self, teacher: TeacherModel) -> None :
        return self.repo_istance.delete(teacher)

class TeacherUpdateService :
    def __init__(self, session):
        self.repo_istance = TeacherRepository(session)
        self.subject_pagination = SubjectPaginationService(session)

    def update(self, changes : TeacherChangeRequest , teacher : TeacherModel ) -> TeacherModel: 
        if changes.subjects : 
            filter_by_subject_ids = SubjectFilterSchema(id=changes.subjects)
            subjects = self.subject_pagination.get_subjects(filter_params=filter_by_subject_ids)
            changes = changes.model_dump(exclude={'subjects'}, exclude_none=True, exclude_unset=True)

        return self.repo_istance.update(changes, teacher, subjects)
        
class TeacherPaginationService :
    def __init__(self, session):
        self.repo_istance = TeacherRepository(session)

    def get_teacher_by_email(self, email: str) -> TeacherTable :
        self.repo_istance.get_teacher_by_email(email)
       
    def get_teacher_by_id(self, id:uuid.UUID ) -> TeacherTable :
        return self.repo_istance.get_by_id(id)
        
    def get_teachers(self, filter_params: TeacherFilterSchema) -> list[TeacherTable] :
        return self.repo_istance.get(filter_params)
        
    def get_teachers_average_better_than_8(self) :
        return self.repo_istance.get_teachers_average_better_than_8()

    def get_teachers_by_technological_classroom(self) : 
        return self.repo_istance.get_teachers_by_technological_classroom()
    
    def get_teachers_by_sanctions(self) :
        return self.repo_istance.get_teachers_by_sanctions()
    
    def get_teachers_by_students(self, student_id: str) :
        return self.repo_istance.get_teachers_by_students(student_id=student_id)
        
class TeacherSubjectService :
    def create_teacher_subject(self, session: Session, teacher_id: str, subject_id: str) :
        teacher_subject = teacher_subject_table.insert().values(teacher_id=teacher_id, subject_id=subject_id)
        session.execute(teacher_subject)
        session.commit()
class TeacherSubjectService :
    def __init__ (self, session) :
        self.repo_instance = TeacherRepository(session)

    def get_teacher_subjects(self, id:uuid.UUID ) -> list[str] :
        return self.repo_instance.get_teacher_subjects(id)
        