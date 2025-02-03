from sqlalchemy.orm import Session
from backend.domain.schemas.administrador import AdministratorCreateModel, AdministratorModel
from backend.domain.filters.administrador import AdministratorChangeRequest, AdministratorFilterSchema, AdministratorFilterSet
from backend.domain.models.tables import AdministratorTable
from sqlalchemy.orm import Session
from sqlalchemy import update, select
import uuid
from backend.application.utils.auth import get_password_hash, get_password
from backend.infrastructure.repositories.administrator import AdministratorRepository

"""
This module defines services for creating, retrieving, updating, and deleting administrator records.

Classes:
    AdministratorCreateService: A service for creating new administrator records.
    AdministratorPaginationService: A service for retrieving administrator records based on various criteria.
    AdministratorDeletionService: A service for deleting administrator records.
    AdministratorUpdateService: A service for updating administrator records.

Classes Details:

1. AdministratorCreateService:
    - This service is responsible for creating new administrator records.
    - It utilizes the AdministratorRepository to interact with the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - create_administrator(administrator: AdministratorCreateModel) -> AdministratorTable: 
            Creates a new administrator record using the provided AdministratorCreateModel and returns the created AdministratorTable object.

2. AdministratorPaginationService:
    - This service is responsible for retrieving administrator records based on different criteria.
    - It uses the AdministratorRepository to fetch data from the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - get_administrator_by_email(email: str) -> AdministratorTable: 
            Retrieves an administrator record by the specified email.
        - get_administrator_by_id(id: uuid.UUID) -> AdministratorTable: 
            Retrieves an administrator record by the specified ID.
        - get(filter_params: AdministratorFilterSchema) -> list[AdministratorTable]: 
            Retrieves a list of administrators based on the provided filter parameters.

3. AdministratorDeletionService:
    - This service is responsible for deleting administrator records.
    - It uses the AdministratorRepository to perform deletion operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - delete_administrator(administrator: AdministratorModel) -> None: 
            Deletes the specified administrator record.

4. AdministratorUpdateService:
    - This service is responsible for updating administrator records.
    - It uses the AdministratorRepository to perform update operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - update_one(changes: AdministratorChangeRequest, administrator: AdministratorModel) -> AdministratorModel: 
            Updates the specified administrator record with the provided changes and returns the updated AdministratorModel.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - AdministratorRepository for database operations related to administrators.
    - AdministratorCreateModel, AdministratorModel, AdministratorTable, and other domain models for data representation.
    - AdministratorFilterSchema and AdministratorFilterSet for filtering administrator records.
    - UUID for handling unique identifiers.
    - Authentication utilities for password management.
"""


class AdministratorCreateService() :
    def __init__(self, session):
        self.repo_instance = AdministratorRepository(session)

    def create_administrator(self, administrator:AdministratorCreateModel) -> AdministratorTable :
        return self.repo_instance.create(administrator)

class AdministratorPaginationService :
    def __init__(self, session):
        self.repo_instance = AdministratorRepository(session)

    def get_administrator_by_email(self,email: str) -> AdministratorTable :
        return self.repo_instance.get_by_email(email)
    
    def get_administrator_by_id(self, id:uuid.UUID ) -> AdministratorTable :
        return self.repo_instance.get_by_id(id)
    
    def get(self, filter_params: AdministratorFilterSchema) -> list[AdministratorTable] :
        return self.repo_instance.get(filter_params)

class AdministratorDeletionService:
    def __init__(self, session):
        self.repo_instance = AdministratorRepository(session)

    def delete_administrator(self, administrator: AdministratorModel) -> None :
        return self.repo_instance.delete(administrator)

class AdministradorUpdateService :
    def __init__ (self, session):
        self.repo_instance = AdministratorRepository(session)

    def update_one(self, changes : AdministratorChangeRequest , administrator : AdministratorModel ) -> AdministratorModel: 
        return self.repo_instance.update(changes, administrator)



   



