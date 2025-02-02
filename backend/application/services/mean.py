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

class MeanCreateService() :
    def __init__ (self, session):
        self.repo_instance = MeanRepository(session)

    def mean_create(self, mean: MeanCreateModel) -> MeanTable :
        return self.repo_instance.create(mean)
    
class MeanDeletionService:
    def __init__ (self, session):
        self.repo_instance = MeanRepository(session)
        
    def delete_mean(self, ean: MeanModel) -> None :
        return self.repo_instance.delete(ean)
        
class MeanUpdateService :
    def __init__ (self, session):
        self.repo_instance = MeanRepository(session)

    def update_one(self, changes : MeanChangeRequest , mean : MeanModel ) -> MeanModel: 
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

  
