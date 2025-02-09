from sqlalchemy.orm import Session
from backend.domain.schemas.mean import MeanCreateModel, MeanModel
from backend.domain.models.tables import MeanTable , TechnologicalMeanTable , TeachingMaterialTable, OthersTable, MeanMaintenanceTable, teacher_request_mean_table
from sqlalchemy import and_
import uuid
from sqlalchemy import select, update, and_
from backend.domain.filters.mean import MeanFilterSet , MeanFilterSchema, MeanChangeRequest
from backend.application.services.classroom import ClassroomPaginationService
from fastapi import HTTPException, status
from backend.infrastructure.repositories.mean import MeanRepository

"""
This module defines services for creating, retrieving, updating, and deleting mean records.

Classes:
    MeanCreateService: A service for creating new mean records.
    MeanDeletionService: A service for deleting mean records.
    MeanUpdateService: A service for updating mean records.
    MeanPaginationService: A service for retrieving mean records based on various criteria.

Classes Details:

1. MeanCreateService:
    - This service is responsible for creating new mean records.
    - It utilizes the MeanRepository to interact with the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - mean_create(mean: MeanCreateModel) -> MeanTable: 
            Creates a new mean record using the provided MeanCreateModel and returns the created MeanTable object.

2. MeanDeletionService:
    - This service is responsible for deleting mean records.
    - It uses the MeanRepository to perform deletion operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - delete_mean(mean: MeanModel) -> None: 
            Deletes the specified mean record.

3. MeanUpdateService:
    - This service is responsible for updating mean records.
    - It uses the MeanRepository to perform update operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - update_one(changes: MeanChangeRequest, mean: MeanModel) -> MeanModel: 
            Updates the specified mean record with the provided changes and returns the updated MeanModel.

4. MeanPaginationService:
    - This service is responsible for retrieving mean records based on different criteria.
    - It uses the MeanRepository to fetch data from the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - get_mean_by_id(id: uuid.UUID) -> MeanTable: 
            Retrieves a mean record by the specified ID.
        - get_means(filter_params: MeanFilterSchema) -> list[MeanTable]: 
            Retrieves a list of means based on the provided filter parameters.
        - get_avaliable_means() -> list[MeanTable]: 
            Retrieves a list of available means.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - MeanRepository for database operations related to means.
    - MeanCreateModel, MeanModel, MeanTable, and other domain models for data representation.
    - MeanFilterSchema and MeanFilterSet for filtering mean records.
    - UUID for handling unique identifiers.
    - FastAPI for handling HTTP exceptions.
"""

class MeanCreateService() :
    def __init__ (self, session):
        self.repo_instance = MeanRepository(session)
        self.classroom_pagination_service = ClassroomPaginationService(session)

    def mean_create(self, mean: MeanCreateModel) -> MeanTable :
        classroom = self.classroom_pagination_service.get_classroom_by_id(id=mean.classroom_id)
        return self.repo_instance.create(mean, classroom=classroom)
    
class MeanDeletionService:
    def __init__ (self, session):
        self.repo_instance = MeanRepository(session)
        
    def delete_mean(self, mean: MeanModel) -> None :
        return self.repo_instance.delete(mean)
        
class MeanUpdateService :
    def __init__ (self, session):
        self.repo_instance = MeanRepository(session)

    def update_one(self, changes : MeanChangeRequest , mean : MeanTable ) -> MeanModel: 
        return self.repo_instance.update(changes, mean)
    
class MeanPaginationService :
    def __init__ (self, session):
        self.repo_instance = MeanRepository(session)

    def get_mean_by_id(self, id:uuid.UUID ) -> MeanTable :
        return self.repo_instance.get_by_id(id)
    
    def get_means(self, filter_params: MeanFilterSchema) -> list[MeanTable] :
        return self.repo_instance.get(filter_params)
        
    def get_avaliable_means(self) -> list[MeanTable] :
        return self.repo_instance.get_avaliable_means()

  
