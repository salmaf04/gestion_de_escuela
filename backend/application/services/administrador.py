from sqlalchemy.orm import Session
from backend.domain.schemas.administrador import AdministratorCreateModel, AdministratorModel
from backend.domain.filters.administrador import AdministratorChangeRequest, AdministratorFilterSchema, AdministratorFilterSet
from backend.domain.models.tables import AdministratorTable
from sqlalchemy.orm import Session
from sqlalchemy import update, select
import uuid
from backend.application.utils.auth import get_password_hash, get_password
from backend.infrastructure.repositories.administrator import AdministratorRepository


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



   



