from sqlalchemy.orm import Session
from backend.domain.schemas.dean import DeanCreateModel, DeanModel
from backend.domain.models.tables import DeanTable
from sqlalchemy import and_, update
import uuid
from sqlalchemy import select
from backend.domain.filters.dean import DeanFilterSet , DeanFilterSchema, DeanChangeRequest
from backend.application.utils.auth import get_password_hash, get_password
from backend.infrastructure.repositories.dean import DeanRepository

"""
This module defines services for creating, retrieving, updating, and deleting dean records.

Classes:
    DeanCreateService: A service for creating new dean records.
    DeanDeletionService: A service for deleting dean records.
    DeanUpdateService: A service for updating dean records.
    DeanPaginationService: A service for retrieving dean records based on various criteria.

Classes Details:

1. DeanCreateService:
    - This service is responsible for creating new dean records.
    - It utilizes the DeanRepository to interact with the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - create_dean(dean: DeanCreateModel) -> DeanTable: 
            Creates a new dean record using the provided DeanCreateModel and returns the created DeanTable object.

2. DeanDeletionService:
    - This service is responsible for deleting dean records.
    - It uses the DeanRepository to perform deletion operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - delete_dean(dean: DeanModel) -> None: 
            Deletes the specified dean record.

3. DeanUpdateService:
    - This service is responsible for updating dean records.
    - It uses the DeanRepository to perform update operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - update_one(changes: DeanChangeRequest, dean: DeanModel) -> DeanModel: 
            Updates the specified dean record with the provided changes and returns the updated DeanModel.

4. DeanPaginationService:
    - This service is responsible for retrieving dean records based on different criteria.
    - It uses the DeanRepository to fetch data from the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - get_dean_by_email(email: str) -> DeanTable: 
            Retrieves a dean record by the specified email.
        - get_dean_by_id(id: uuid.UUID) -> DeanTable: 
            Retrieves a dean record by the specified ID.
        - get_dean(filter_params: DeanFilterSchema) -> list[DeanTable]: 
            Retrieves a list of deans based on the provided filter parameters.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - DeanRepository for database operations related to deans.
    - DeanCreateModel, DeanModel, DeanTable, and other domain models for data representation.
    - DeanFilterSchema and DeanFilterSet for filtering dean records.
    - UUID for handling unique identifiers.
    - Authentication utilities for password management.
"""

class DeanCreateService :
    def __init__(self, session):
        self.repo_instance = DeanRepository(session)

    def create_dean(self, dean: DeanCreateModel) -> DeanTable :
        return self.repo_instance.create(dean)
    
class DeanDeletionService:
    def __init__(self, session):
        self.repo_instance = DeanRepository(session)
        
    def delete_dean(self,dean: DeanModel) -> None :
        return self.repo_instance.delete(dean)
        
class DeanUpdateService :
    def __init__(self, session):
        self.repo_instance = DeanRepository(session)

    def update_one(self, changes : DeanChangeRequest , dean : DeanModel ) -> DeanModel: 
        return self.repo_instance.update(changes, dean)
        
class DeanPaginationService :
    def __init__(self, session):    
        self.repo_instance = DeanRepository(session)

    def get_dean_by_email(self, email: str) -> DeanTable :
        return self.repo_instance.get_by_email(email)
    
    def get_dean_by_id(self, id:uuid.UUID ) -> DeanTable :
        return self.repo_instance.get_by_id(id)
    
    def get_dean(self, filter_params: DeanFilterSchema) -> list[DeanTable] :
        return self.repo_instance.get(filter_params) 