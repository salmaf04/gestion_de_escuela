from sqlalchemy.orm import Session
from backend.domain.schemas.administrador import AdministratorCreateModel, AdministratorModel
from backend.domain.filters.administrador import ChangeRequest
from backend.domain.models.tables import AdministratorTable
from sqlalchemy.orm import Session
from sqlalchemy import update
import uuid

class AdministratorCreateService :

    def create_administrator(self, session: Session, administrator:AdministratorCreateModel) -> AdministratorTable :
        administrator_dict = administrator.model_dump()

        new_administrator = AdministratorTable(**administrator_dict)
        session.add(new_administrator)
        session.commit()
        return new_administrator

    

class AdministratorPaginationService :
    def get_administrator_by_email(self, session: Session, email: str) -> AdministratorTable :
        query = session.query(AdministratorTable).filter(AdministratorTable.email == email)

        result = query.first()

        return result
    
    def get_administrator_by_id(self, session: Session, id:uuid.UUID ) -> AdministratorTable :
        query = session.query(AdministratorTable).filter(AdministratorTable.entity_id == id)

        result = query.scalar()

        return result

    
class AdministratorDeletionService:
    def delete_administrator(self, session: Session, administrator: AdministratorModel) -> None :
        session.delete(administrator)
        session.commit()


class AdministradorUpdateService :
    def update_one(self, session : Session , changes : ChangeRequest , administrator : AdministratorModel ) -> AdministratorModel: 
        query = update(AdministratorTable).where(AdministratorTable.entity_id == administrator.id)
        
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        session.execute(query)
        session.commit()
        
        administrator = administrator.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return administrator



   



