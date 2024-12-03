from sqlalchemy.orm import Session
from sqlalchemy import update
from .filters import ChangeRequest
from database.tables import SecretaryTable
from secretary.secretary_common.schemas import  SecretaryModel

class SecretaryUpdateService :
    def update_one(self, session : Session , changes : ChangeRequest , secretary : SecretaryModel ) -> SecretaryModel: 
        query = update(SecretaryTable).where(SecretaryTable.entity_id == secretary.id)
        
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        session.execute(query)
        session.commit()
        
        secretary = secretary.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return secretary

class SecretaryListingService :
    def get_secretary_by_id(self, session: Session, id : int) -> SecretaryTable :
        query = session.query(SecretaryTable).filter(SecretaryTable.entity_id == id)

        result = query.first()

        return result