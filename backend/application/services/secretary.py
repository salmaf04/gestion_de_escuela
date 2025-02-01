from sqlalchemy.orm import Session
from backend.domain.schemas.secretary import SecretaryCreateModel, SecretaryModel
from backend.domain.models.tables import SecretaryTable
import uuid
from sqlalchemy import update
from backend.domain.filters.secretary import SecretaryChangeRequest
from ..utils.auth import get_password_hash, get_password

class SecretaryCreateService :

    def create_secretary(self, session: Session, secretary:SecretaryCreateModel) -> SecretaryTable :
        secretary_dict = secretary.model_dump(exclude={'password'})
        hashed_password = get_password_hash(get_password(secretary))
        new_secretary = SecretaryTable(**secretary_dict, hashed_password=hashed_password)
        session.add(new_secretary)
        session.commit()
        return new_secretary

    
class SecretaryDeletionService:
    def delete_secretary(self, session: Session, secretary: SecretaryModel) -> None :
        session.delete(secretary)
        session.commit()
        

class SecretaryUpdateService :
    def update_one(self, session : Session , changes : SecretaryChangeRequest , secretary : SecretaryModel ) -> SecretaryModel: 
        query = update(SecretaryTable).where(SecretaryTable.entity_id == secretary.id)
        
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        session.execute(query)
        session.commit()
        
        secretary = secretary.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return secretary
    
        
class SecretaryPaginationService :
    def get_secretary_by_email(self, session: Session, email: str) -> SecretaryTable :
        query = session.query(SecretaryTable).filter(SecretaryTable.email == email)

        result = query.first()

        return result
    
    def get_secretary_by_id(self, session: Session, id:uuid.UUID ) -> SecretaryTable :
        query = session.query(SecretaryTable).filter(SecretaryTable.entity_id == id)

        result = query.scalar()

        return result
    



    



