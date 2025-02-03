from sqlalchemy.orm import Session
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.mean import MeanPaginationService
from backend.infrastructure.repositories.mean_request import MeanRequestRepository

"""
This module defines services for creating, retrieving, and deleting mean requests.

Classes:
    MeanRequestCreateService: A service for creating new mean requests.
    MeanRequestPaginationService: A service for retrieving mean requests based on specific criteria.
    MeanRequestDeletionService: A service for deleting mean requests.

Classes Details:

1. MeanRequestCreateService:
    - This service is responsible for creating new mean requests.
    - It utilizes the MeanRequestRepository to interact with the database.
    - It also uses TeacherPaginationService and MeanPaginationService to retrieve teacher and mean details.
    
    Methods:
        - __init__(session): Initializes the service with a database session and sets up necessary service instances.
        - create_mean_request(mean_id: str, teacher_id: str): 
            Creates a new mean request using the specified mean and teacher IDs.

2. MeanRequestPaginationService:
    - This service is responsible for retrieving mean requests based on specific criteria.
    - It uses the MeanRequestRepository to fetch data from the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - get_by_id(teacher_id: str, mean_id: str): 
            Retrieves a mean request by the specified teacher and mean IDs.

3. MeanRequestDeletionService:
    - This service is responsible for deleting mean requests.
    - It uses the MeanRequestRepository to perform deletion operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - delete(mean_request): 
            Deletes the specified mean request.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - MeanRequestRepository for database operations related to mean requests.
    - TeacherPaginationService and MeanPaginationService for retrieving teacher and mean information.
"""

class MeanRequestCreateService :
    def __init__(self, session):
        self.repo_instance = MeanRequestRepository(session)
        self.teacher_pagination_service = TeacherPaginationService(session)
        self.mean_pagination_service = MeanPaginationService(session)

    def create_mean_request(self, mean_id: str, teacher_id: str) :
        mean = self.mean_pagination_service.get_mean_by_id(id=mean_id)
        teacher = self.teacher_pagination_service.get_teacher_by_id(id=teacher_id)
        return self.repo_instance.create(mean=mean, teacher=teacher)
    
class MeanRequestPaginationService :
    def __init__(self, session) :
        self.repo_instance = MeanRequestRepository(session)

    def get_by_id(self, teacher_id: str, mean_id: str ) :
        return self.repo_instance.get_by_id(teacher_id=teacher_id, mean_id=mean_id)

class MeanRequestDeletionService :
    def __init__(self, session) :
        self.repo_instance = MeanRequestRepository(session)

    def delete(self, mean_request ) :
        return self.repo_instance.delete(entity=None, mean_request=mean_request)
