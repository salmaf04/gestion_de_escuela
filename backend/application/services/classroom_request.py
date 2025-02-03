from sqlalchemy.orm import Session
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.classroom import ClassroomPaginationService
from backend.domain.models.tables import TeacherTable, ClassroomTable
from backend.infrastructure.repositories.classroom_request import ClassroomRequestRepository

"""
This module defines services for creating, retrieving, and deleting classroom requests.

Classes:
    ClassroomRequestCreateService: A service for creating new classroom requests.
    ClassroomRequestPaginationService: A service for retrieving classroom requests based on specific criteria.
    ClassroomRequestDeletionService: A service for deleting classroom requests.

Classes Details:

1. ClassroomRequestCreateService:
    - This service is responsible for creating new classroom requests.
    - It utilizes the ClassroomRequestRepository to interact with the database.
    - It also uses TeacherPaginationService and ClassroomPaginationService to retrieve teacher and classroom details.
    
    Methods:
        - __init__(session): Initializes the service with a database session and sets up necessary service instances.
        - create_classroom_request(teacher_id: str, classroom_id: str): 
            Creates a new classroom request using the specified teacher and classroom IDs.

2. ClassroomRequestPaginationService:
    - This service is responsible for retrieving classroom requests based on specific criteria.
    - It uses the ClassroomRequestRepository to fetch data from the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - get_by_id(teacher_id: str, classroom_id: str): 
            Retrieves a classroom request by the specified teacher and classroom IDs.

3. ClassroomRequestDeletionService:
    - This service is responsible for deleting classroom requests.
    - It uses the ClassroomRequestRepository to perform deletion operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - delete(classroom_request): 
            Deletes the specified classroom request.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - ClassroomRequestRepository for database operations related to classroom requests.
    - TeacherPaginationService and ClassroomPaginationService for retrieving teacher and classroom information.
    - TeacherTable and ClassroomTable for data representation.
"""

class ClassroomRequestCreateService :
    def __init__(self, session):
        self.session = session
        self.repo_instance = ClassroomRequestRepository(session)
        self.teacher_pagination_service = TeacherPaginationService(session)
        self.classroom_pagination_service = ClassroomPaginationService(session)

    def create_classroom_request(self, teacher_id : str, classroom_id : str) :
        teacher = self.teacher_pagination_service.get_teacher_by_id(id=teacher_id)
        classroom = self.classroom_pagination_service.get_classroom_by_id(id=classroom_id)
        return self.repo_instance.create(teacher, classroom)

class ClassroomRequestPaginationService :
    def __init__(self, session) :
        self.repo_instance = ClassroomRequestRepository(session)

    def get_by_id(self, teacher_id: str, classroom_id : str ) :
        return self.repo_instance.get_by_id(teacher_id=teacher_id, classroom_id=classroom_id)

class ClassroomRequestDeletionService :
    def __init__(self, session) :
        self.repo_instance = ClassroomRequestRepository(session)

    def delete(self, classroom_request ) :
        return self.repo_instance.delete(entity=None, classroom_request=classroom_request)
