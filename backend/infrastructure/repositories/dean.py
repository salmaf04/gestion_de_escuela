from sqlalchemy.orm import Session
from backend.domain.schemas.dean import DeanCreateModel, DeanModel
from backend.domain.models.tables import DeanTable
from sqlalchemy import and_, update
import uuid
from sqlalchemy import select
from backend.domain.filters.dean import DeanFilterSet , DeanFilterSchema, DeanChangeRequest
from ..utils.auth import get_password_hash, get_password
from .. import IRepository

class DeanRepository(IRepository[DeanCreateModel, DeanModel, DeanChangeRequest, DeanFilterSchema]):
    def __init__(self, session):
        super().__init__(session)

    def create(self, entity: DeanCreateModel) -> DeanTable :
        dean_dict = entity.model_dump(exclude={'password'})
        hashed_password = get_password_hash(get_password(entity))
        new_dean = DeanTable(**dean_dict, hashed_password=hashed_password)
        self.session.add(new_dean)
        self.session.commit()
        return new_dean
    
    def delete(self, entity: DeanModel) -> None :
        self.session.delete(entity)
        self.session.commit()

    def update(self, changes : DeanChangeRequest , entity : DeanModel) -> DeanModel:
        query = update(DeanTable).where(DeanTable.entity_id == entity.id)
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        self.session.execute(query)
        self.session.commit()
        
        dean = entity.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return dean
        
    def get_by_id(self, id: str ) -> DeanTable :    
        query = self.session.query(DeanTable).filter(DeanTable.entity_id == id)
        result = query.scalar() 
        return result
    
    def get(self, filter_params: DeanFilterSchema) -> list[DeanTable] :
        query = select(DeanTable)
        filter_set = DeanFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return self.session.execute(query).scalars().all()

    def get_by_email(self, email: str) -> DeanTable :
        query = self.session.query(DeanTable).filter(DeanTable.email == email)

        result = query.first()

        return result
    
 