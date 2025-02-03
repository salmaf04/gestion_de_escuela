from sqlalchemy.orm import Session
from backend.domain.schemas.dean import DeanCreateModel, DeanModel
from backend.domain.models.tables import DeanTable
from sqlalchemy import and_, update
import uuid
from sqlalchemy import select
from backend.domain.filters.dean import DeanFilterSet , DeanFilterSchema, DeanChangeRequest
from backend.application.utils.auth import get_password_hash, get_password
from backend.infrastructure.repositories.dean import DeanRepository


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