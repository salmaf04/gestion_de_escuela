from sqlalchemy.orm import Session
from backend.domain.schemas.mean_maintenance import MeanMaintenanceCreateModel, MeanMaintenanceModel
from backend.domain.models.tables import MeanMaintenanceTable
from sqlalchemy import select, update
from backend.application.services.mean import MeanPaginationService
from backend.application.services.my_date import DatePaginationService
from backend.domain.filters.mean_maintenance import MeanMaintenanceFilterSet , MeanMaintenanceFilterSchema,  MeanMaintenanceChangeRequest
from backend.domain.models.tables import MeanMaintenanceTable, TechnologicalMeanTable, MeanTable, ClassroomTable
import uuid
from datetime import datetime, timedelta, timezone
from sqlalchemy import func
from sqlalchemy import extract, and_
from backend.infrastructure.repositories.mean_maintenance import MeanMaintenanceRepository

"""
This module defines services for creating, retrieving, and updating mean maintenance records.

Classes:
    MeanMaintenanceCreateService: A service for creating new mean maintenance records.
    MeanMaintenancePaginationService: A service for retrieving mean maintenance records based on various criteria.
    MeanMaintenanceUpdateService: A service for updating mean maintenance records.

Classes Details:

1. MeanMaintenanceCreateService:
    - This service is responsible for creating new mean maintenance records.
    - It utilizes the MeanMaintenanceRepository to interact with the database.
    - It also uses MeanPaginationService to retrieve mean details.
    
    Methods:
        - __init__(session): Initializes the service with a database session and sets up necessary service instances.
        - create_mean_maintenance(mean_maintenance: MeanMaintenanceCreateModel) -> MeanMaintenanceTable: 
            Creates a new mean maintenance record using the provided MeanMaintenanceCreateModel and returns the created MeanMaintenanceTable object.

2. MeanMaintenancePaginationService:
    - This service is responsible for retrieving mean maintenance records based on different criteria.
    - It uses the MeanMaintenanceRepository to fetch data from the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - get_mean_maintenance(filter_params: MeanMaintenanceFilterSchema) -> list[MeanMaintenanceTable]: 
            Retrieves a list of mean maintenance records based on the provided filter parameters.
        - get_mean_maintenance_by_id(id: str) -> MeanMaintenanceTable: 
            Retrieves a mean maintenance record by the specified ID.
        - get_mainenance_by_classroom(): 
            Retrieves maintenance records grouped by classroom.
        - maintenace_average(): 
            Calculates and retrieves the average maintenance statistics.
        - maintenance_by_classroom(): 
            Retrieves maintenance records organized by classroom.

3. MeanMaintenanceUpdateService:
    - This service is responsible for updating mean maintenance records.
    - It uses the MeanMaintenanceRepository to perform update operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - update_one(changes: MeanMaintenanceChangeRequest, mean_maintenance: MeanMaintenanceModel) -> MeanMaintenanceModel: 
            Updates the specified mean maintenance record with the provided changes and returns the updated MeanMaintenanceModel.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - MeanMaintenanceRepository for database operations related to mean maintenance.
    - MeanMaintenanceCreateModel, MeanMaintenanceModel, MeanMaintenanceTable, and other domain models for data representation.
    - MeanMaintenanceFilterSchema and MeanMaintenanceFilterSet for filtering mean maintenance records.
    - MeanPaginationService for retrieving mean information.
    - UUID and datetime for handling unique identifiers and date-time operations.
"""

class MeanMaintenanceCreateService :
    def __init__ (self, session):
        self.repo_instance = MeanMaintenanceRepository(session)
        self.mean_pagination_service = MeanPaginationService(session)

    def create_mean_maintenance(self, mean_maintenance:MeanMaintenanceCreateModel) -> MeanMaintenanceTable :
        
        mean = self.mean_pagination_service.get_mean_by_id(id=mean_maintenance.mean_id)
        return self.repo_instance.create(mean_maintenance, mean)
       
class MeanMaintenancePaginationService :
    def __init__ (self, session):
        self.repo_instance = MeanMaintenanceRepository(session)

    def get_mean_maintenance(self, filter_params: MeanMaintenanceFilterSchema) -> list[MeanMaintenanceTable] :
        return self.repo_instance.get(filter_params)
      
    
    def get_mean_maintenance_by_id(self, id: str) -> MeanMaintenanceTable :
        return self.repo_instance.get_by_id(id)
    

    def get_mainenance_by_classroom(self) :
        return self.repo_instance.get_mainenance_by_classroom()
        
    def maintenace_average(self) :
        return self.repo_instance.maintenace_average()

    def maintenance_by_classroom(self) :
        return self.repo_instance.maintenance_by_classroom()
       
class MeanMaintenanceUpdateService :
    def __init__(self, session):
        self.repo_instance = MeanMaintenanceRepository(session)

    def update_one(self, changes : MeanMaintenanceChangeRequest , mean_maintenance : MeanMaintenanceModel ) -> MeanMaintenanceModel:
        return self.repo_instance.update(changes, mean_maintenance)
      

    