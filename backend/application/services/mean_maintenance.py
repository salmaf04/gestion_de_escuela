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
      

    