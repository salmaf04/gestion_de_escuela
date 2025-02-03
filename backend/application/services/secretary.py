from sqlalchemy.orm import Session
from backend.domain.schemas.secretary import SecretaryCreateModel, SecretaryModel
from backend.domain.models.tables import SecretaryTable
import uuid
from sqlalchemy import update, select
from backend.domain.filters.secretary import SecretaryChangeRequest, SecretaryFilterSchema, SecretaryFilterSet
from backend.infrastructure.repositories.secretary import SecretaryRepository

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


    



