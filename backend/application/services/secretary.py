from sqlalchemy.orm import Session
from backend.domain.schemas.secretary import SecretaryCreateModel, SecretaryModel
from backend.domain.models.tables import SecretaryTable
import uuid
from sqlalchemy import update, select
from backend.domain.filters.secretary import SecretaryChangeRequest, SecretaryFilterSchema, SecretaryFilterSet
from backend.infrastructure.repositories.secretary import SecretaryRepository

"""
This module defines services for creating, retrieving, updating, and deleting secretary records.

Classes:
    SecretaryCreateService: A service for creating new secretary records.
    SecretaryDeletionService: A service for deleting secretary records.
    SecretaryUpdateService: A service for updating secretary records.
    SecretaryPaginationService: A service for retrieving secretary records based on various criteria.

Classes Details:

1. SecretaryCreateService:
    - This service is responsible for creating new secretary records.
    - It utilizes the SecretaryRepository to interact with the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - create_secretary(secretary: SecretaryCreateModel) -> SecretaryTable: 
            Creates a new secretary record using the provided SecretaryCreateModel and returns the created SecretaryTable object.

2. SecretaryDeletionService:
    - This service is responsible for deleting secretary records.
    - It uses the SecretaryRepository to perform deletion operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - delete_secretary(secretary: SecretaryModel) -> None: 
            Deletes the specified secretary record.

3. SecretaryUpdateService:
    - This service is responsible for updating secretary records.
    - It uses the SecretaryRepository to perform update operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - update_one(changes: SecretaryChangeRequest, secretary: SecretaryModel) -> SecretaryModel: 
            Updates the specified secretary record with the provided changes and returns the updated SecretaryModel.

4. SecretaryPaginationService:
    - This service is responsible for retrieving secretary records based on different criteria.
    - It uses the SecretaryRepository to fetch data from the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - get_secretary_by_email(email: str) -> SecretaryTable: 
            Retrieves a secretary record by the specified email.
        - get_secretary_by_id(id: uuid.UUID) -> SecretaryTable: 
            Retrieves a secretary record by the specified ID.
        - get(filter_params: SecretaryFilterSchema) -> list[SecretaryTable]: 
            Retrieves a list of secretaries based on the provided filter parameters.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - SecretaryRepository for database operations related to secretaries.
    - SecretaryCreateModel, SecretaryModel, SecretaryTable, and other domain models for data representation.
    - SecretaryFilterSchema and SecretaryFilterSet for filtering secretary records.
    - UUID for handling unique identifiers.
"""

class SecretaryCreateService :
    def __init__(self, session):
        self.repo_instance = SecretaryRepository(session)

    def create_secretary(self,secretary:SecretaryCreateModel) -> SecretaryTable :
        return self.repo_instance.create(secretary)

    
class SecretaryDeletionService:
    def __init__(self, session):
        self.repo_instance = SecretaryRepository(session)

    def delete_secretary(self,secretary: SecretaryModel) -> None :
        return self.repo_instance.delete(secretary)
        

class SecretaryUpdateService :
    def __init__(self, session):
        self.repo_instance = SecretaryRepository(session)

    def update_one(self, changes : SecretaryChangeRequest , secretary : SecretaryModel ) -> SecretaryModel: 
        return self.repo_instance.update(changes, secretary)
    
class SecretaryPaginationService :
    def __init__(self, session):
        self.repo_instance = SecretaryRepository(session)

    def get_secretary_by_email(self, email: str) -> SecretaryTable :
        return self.repo_instance.get_secretary_by_email(email)
    
    def get_secretary_by_id(self, id:uuid.UUID ) -> SecretaryTable :
        return self.repo_instance.get_by_id(id)
    
    def get(self, filter_params: SecretaryFilterSchema) -> list[SecretaryTable] :
        return self.repo_instance.get(filter_params)


    



