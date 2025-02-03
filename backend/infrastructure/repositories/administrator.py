from sqlalchemy.orm import Session
from backend.domain.schemas.administrador import AdministratorCreateModel, AdministratorModel
from backend.domain.filters.administrador import AdministratorChangeRequest, AdministratorFilterSchema, AdministratorFilterSet
from backend.domain.models.tables import AdministratorTable
from sqlalchemy.orm import Session
from sqlalchemy import update, select
import uuid
from backend.application.utils.auth import get_password_hash, get_password
from .base import IRepository

class AdministratorRepository(IRepository[AdministratorCreateModel,AdministratorModel, AdministratorChangeRequest,AdministratorFilterSchema]):
    def __init__(self, session):
        super().__init__(session)

    def create(self, entity: AdministratorCreateModel) -> AdministratorTable :
        administrator_dict = entity.model_dump(exclude={'password'})
        hashed_password = get_password_hash(get_password(entity))
        new_administrator = AdministratorTable(**administrator_dict, hashed_password=hashed_password)
        self.session.add(new_administrator)
        self.session.commit()
        return new_administrator
    
    def delete(self, entity: AdministratorModel) -> None :
        self.session.delete(entity)
        self.session.commit()

    def update(self, changes : AdministratorChangeRequest , entity : AdministratorModel ) -> AdministratorModel:
        query = update(AdministratorTable).where(AdministratorTable.entity_id == entity.id)
        
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        self.session.execute(query)
        self.session.commit()
        
        administrator = entity.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return administrator
    
    def get(self, filter_params: AdministratorFilterSchema) -> list[AdministratorTable] :
        query = select(AdministratorTable)
        filter_set = AdministratorFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return self.session.execute(query).scalars().all()
    
    def get_by_id(self, id: str ) -> AdministratorTable :
        query = self.session.query(AdministratorTable).filter(AdministratorTable.entity_id == id)

        result = query.scalar()

        return result
    
    def get_by_email(self, email: str ) -> AdministratorTable :
        query = self.session.query(AdministratorTable).filter(AdministratorTable.email == email)

        result = query.scalar()

        return result
    



   
