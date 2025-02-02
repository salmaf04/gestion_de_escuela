from sqlalchemy.orm import Session
from backend.domain.schemas.secretary import SecretaryCreateModel, SecretaryModel
from backend.domain.models.tables import SecretaryTable
import uuid
from sqlalchemy import update, select
from backend.domain.filters.secretary import SecretaryChangeRequest, SecretaryFilterSchema, SecretaryFilterSet
from ..utils.auth import get_password_hash, get_password
from .. import IRepository

class SecretaryRepository(IRepository[SecretaryCreateModel,SecretaryModel, SecretaryChangeRequest,SecretaryFilterSchema]):
    def __init__(self, session):
        super().__init__(session)

    def create(self, entity: SecretaryCreateModel) -> SecretaryTable :
        secretary_dict = entity.model_dump(exclude={'password'})
        hashed_password = get_password_hash(get_password(entity))
        new_secretary = SecretaryTable(**secretary_dict, hashed_password=hashed_password)
        self.session.add(new_secretary)
        self.session.commit()
        return new_secretary

    def delete(self, entity: SecretaryModel) -> None :
        self.session.delete(entity)
        self.session.commit()

    def update(self, changes : SecretaryChangeRequest , entity : SecretaryModel ) -> SecretaryModel:
        query = update(SecretaryTable).where(SecretaryTable.entity_id == entity.id)
        
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        self.session.execute(query)
        self.session.commit()
        
        secretary = entity.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return secretary
    
    def get_by_id(self, id: str ) -> SecretaryTable :
        query = self.session.query(SecretaryTable).filter(SecretaryTable.entity_id == id)

        result = query.scalar()

        return result
    
    def get(self, filter_params: SecretaryFilterSchema) -> list[SecretaryTable] :
        query = select(SecretaryTable)
        filter_set = SecretaryFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return self.session.execute(query).scalars().all()


    def get_secretary_by_email(self, email: str) -> SecretaryTable :
        query = self.session.query(SecretaryTable).filter(SecretaryTable.email == email)

        result = query.first()

        return result
    