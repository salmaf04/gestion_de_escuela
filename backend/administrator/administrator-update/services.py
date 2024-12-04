from sqlalchemy.orm import Session
from sqlalchemy import update
from .filters import ChangeRequest
from database.tables import AdministratorTable
from administrator.administrator_common.schemas import  AdministratorModel

class SecretaryUpdateService :
    def update_one(self, session : Session , changes : ChangeRequest , administrator : AdministratorModel ) -> AdministratorModel: 
        query = update(AdministratorTable).where(AdministratorTable.entity_id == administrator.id)
        
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        session.execute(query)
        session.commit()
        
        administrator = administrator.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return administrator

class AdministratorListingService :
    def get_administrator_by_id(self, session: Session, id : int) -> AdministratorTable :
        query = session.query(AdministratorTable).filter(AdministratorTable.entity_id == id)

        result = query.first()

        return result