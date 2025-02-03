from sqlalchemy.orm import Session
from backend.domain.models.tables import SanctionTable
from backend.domain.schemas.sanction import SanctionCreateModel
from backend.application.services.teacher import TeacherPaginationService
from backend.infrastructure.repositories.sanction import SanctionRepository

"""
This module defines a service for creating sanction records.

Classes:
    SanctionCreateService: A service for creating new sanction records.

Class Details:

SanctionCreateService:
    - This service is responsible for creating new sanction records.
    - It utilizes the SanctionRepository to interact with the database.
    - It also uses TeacherPaginationService to retrieve teacher details associated with the sanction.
    
    Methods:
        - __init__(session): Initializes the service with a database session and sets up necessary service instances.
        - create_sanction(sanction: SanctionCreateModel) -> SanctionTable: 
            Creates a new sanction record using the provided SanctionCreateModel and returns the created SanctionTable object.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - SanctionRepository for database operations related to sanctions.
    - SanctionCreateModel and SanctionTable for data representation.
    - TeacherPaginationService for retrieving teacher information.
"""

class SanctionCreateService : 
    def __init__(self, session):
        self.repo_instance = SanctionRepository(session)
        self.teacher_pagination_service = TeacherPaginationService(session)

    def create_sanction(self, sanction: SanctionCreateModel) -> SanctionTable :
        teacher = self.teacher_pagination_service.get_teacher_by_id(id=sanction.teacher_id)
        return self.repo_instance.create(sanction, teacher)
