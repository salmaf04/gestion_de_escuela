from sqlalchemy.orm import Session
from backend.domain.schemas.dean import DeanCreateModel, DeanModel
from backend.domain.models.tables import DeanTable
from sqlalchemy import and_, update
import uuid
from sqlalchemy import select
from backend.domain.filters.dean import DeanFilterSet , DeanFilterSchema, ChangeRequest
from ..utils.auth import get_password_hash


class DeanCreateService :

    def create_dean(self, session: Session, dean: DeanCreateModel) -> DeanTable :
        dean_dict = dean.model_dump(exclude={'password'})
        hashed_password = get_password_hash(dean.password)
        new_dean = DeanTable(**dean_dict, hash_password=hashed_password)
        session.add(new_dean)
        session.commit()
        return new_dean
    
    
class DeanDeletionService:
    def delete_dean(self, session: Session, dean: DeanModel) -> None :
        session.delete(dean)
        session.commit()
        
        
class DeanUpdateService :
    def update_one(self, session : Session , changes : ChangeRequest , dean : DeanModel ) -> DeanModel: 
        query = update(DeanTable).where(DeanTable.entity_id == dean.id)
        
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        session.execute(query)
        session.commit()
        
        dean = dean.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return dean
        

class DeanPaginationService :
    def get_dean_by_email(self, session: Session, email: str) -> DeanTable :
        query = session.query(DeanTable).filter(DeanTable.email == email)

        result = query.first()

        return result
    
    def get_dean_by_id(self, session: Session, id:uuid.UUID ) -> DeanTable :
        query = session.query(DeanTable).filter(DeanTable.entity_id == id)

        result = query.scalar()

        return result
    
    def get_dean(self, session: Session, filter_params: DeanFilterSchema) -> list[DeanTable] :
        query = select(DeanTable)
        filter_set = DeanFilterSet(session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return session.scalars(query).all()