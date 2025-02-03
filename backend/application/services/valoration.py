from sqlalchemy.orm import Session
from backend.domain.schemas.valoration import ValorationCreateModel
from backend.domain.models.tables import TeacherNoteTable, TeacherTable, StudentTable, SubjectTable, CourseTable
from backend.application.services.student import StudentPaginationService
from backend.application.services.subject import SubjectPaginationService
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.course import CoursePaginationService
from backend.domain.filters.valoration import ValorationFilterSchema, ValorationFilterSet
from sqlalchemy import select, func, update
from backend.infrastructure.repositories.valoration import ValorationRepository

"""
This module defines services for creating and retrieving valoration records.

Classes:
    ValorationCreateService: A service for creating new valoration records.
    ValorationPaginationService: A service for retrieving valoration records based on various criteria.

Classes Details:

1. ValorationCreateService:
    - This service is responsible for creating new valoration records.
    - It utilizes the ValorationRepository to interact with the database.
    - It also uses TeacherPaginationService, StudentPaginationService, SubjectPaginationService, and CoursePaginationService to retrieve related details.
    
    Methods:
        - __init__(session): Initializes the service with a database session and sets up necessary service instances.
        - create_valoration(valoration: ValorationCreateModel) -> TeacherNoteTable: 
            Creates a new valoration record using the provided ValorationCreateModel and returns the created TeacherNoteTable object.

2. ValorationPaginationService:
    - This service is responsible for retrieving valoration records based on different criteria.
    - It uses the ValorationRepository to fetch data from the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - get_valoration(filter_params: ValorationFilterSchema) -> list[TeacherNoteTable]: 
            Retrieves a list of valorations based on the provided filter parameters.
        - get_valoration_by_teacher_id(teacher_id: str): 
            Retrieves valorations associated with a specific teacher identified by the teacher_id.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - ValorationRepository for database operations related to valorations.
    - ValorationCreateModel, TeacherNoteTable, and other domain models for data representation.
    - ValorationFilterSchema and ValorationFilterSet for filtering valoration records.
    - TeacherPaginationService, StudentPaginationService, SubjectPaginationService, and CoursePaginationService for retrieving related information.
"""

class ValorationCreateService :
    def __init__(self, session):
        self.repo_instance = ValorationRepository(session)
        self.teacher_pagination_service = TeacherPaginationService(session)
        self.student_pagination_service = StudentPaginationService(session)
        self.subject_pagination_service = SubjectPaginationService(session)
        self.course_pagination_service = CoursePaginationService(session)

    def create_valoration(
        self, 
        valoration: ValorationCreateModel,
    ) -> TeacherNoteTable : 
        return self.repo_instance.create(
            valoration=valoration,
            student=self.student_pagination_service.get_student_by_id(id=valoration.student_id),
            subject=self.subject_pagination_service.get_subject_by_id(id=valoration.subject_id),
            teacher=self.teacher_pagination_service.get_teacher_by_id(id=valoration.teacher_id),
            course=self.course_pagination_service.get_course_by_id(id=valoration.course_id)
        )
        
class ValorationPaginationService :
    def __init__(self, session):
        self.repo_instance = ValorationRepository(session)

    def get_valoration(self, filter_params: ValorationFilterSchema) -> list[TeacherNoteTable] :
        return self.repo_instance.get(filter_params)
        

    def get_valoration_by_teacher_id(self, teacher_id: str) :
        return self.repo_instance.get_valoration_by_teacher_id(teacher_id)
