from sqlalchemy.orm import Session
from sqlalchemy import select, func
from backend.domain.schemas.absence import AbsenceCreateModel
from backend.domain.models.tables import AbsenceTable, StudentTable, SubjectTable, TeacherTable, CourseTable, teacher_subject_table
from backend.application.services.student import StudentPaginationService
from backend.application.services.course import CoursePaginationService
from backend.application.services.subject import SubjectPaginationService
from backend.domain.filters.absence import AbsenceFilterSchema, AbsenceFilterSet
from datetime import datetime
import uuid
from  backend.infrastructure.repositories.absence import AbsenceRepository

"""
This module defines services for creating and listing student absences.

Classes:
    AbsenceCreateService: A service for creating student absences.
    AbsencePaginationService: A service for retrieving student absences based on various filters.

Classes Details:

1. AbsenceCreateService:
    - This service is responsible for creating new absence records for students.
    - It utilizes the AbsenceRepository to interact with the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - create_absence(absence: AbsenceCreateModel) -> AbsenceTable: 
            Creates a new absence record using the provided AbsenceCreateModel and returns the created AbsenceTable object.

2. AbsencePaginationService:
    - This service is responsible for retrieving absence records based on different criteria.
    - It also uses the AbsenceRepository to fetch data from the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - get_absence(filter_params: AbsenceFilterSchema) -> list[AbsenceTable]: 
            Retrieves a list of absences based on the provided filter parameters.
        - get_absence_by_student(student_id: uuid.UUID) -> list[AbsenceTable]: 
            Retrieves a list of absences for a specific student identified by the student_id.
        - get_absence_by_student_by_teacher(teacher_id: uuid.UUID) -> list[AbsenceTable]: 
            Retrieves a list of absences for students taught by a specific teacher identified by the teacher_id.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - AbsenceRepository for database operations related to absences.
    - AbsenceCreateModel, AbsenceTable, and other domain models for data representation.
    - AbsenceFilterSchema and AbsenceFilterSet for filtering absence records.
    - UUID and datetime for handling unique identifiers and date-time operations.
"""

class AbsenceCreateService :
    def __init__(self, session):
        self.repo_instance = AbsenceRepository(session)

    def create_absence(self, absence:AbsenceCreateModel) -> AbsenceTable :
        return self.repo_instance.create(absence)
    
class AbsencePaginationService :
    def __init__(self, session):
        self.repo_instance = AbsenceRepository(session)

    def get_absence(self, filter_params: AbsenceFilterSchema) -> list[AbsenceTable] :
        return self.repo_instance.get(filter_params)
    
    def get_absence_by_student(self,  student_id: uuid.UUID) -> list[AbsenceTable] :
        return self.repo_instance.get_absence_by_student(student_id)
    
    def get_absence_by_student_by_teacher(self, teacher_id: uuid.UUID) -> list[AbsenceTable] :
        return self.repo_instance.get_absence_by_student_by_teacher(teacher_id)

