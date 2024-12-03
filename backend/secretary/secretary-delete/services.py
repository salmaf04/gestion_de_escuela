from secretary.secretary_common.schemas import SecretaryModel
from sqlalchemy.orm import Session
from database.tables import SecretaryTable
import uuid

class SecretaryDeletionService:
    def delete_secretary(self, session: Session, secretary: SecretaryModel) -> None :
        session.delete(secretary)
        session.commit()

class SecretaryPaginationService :
    def get_secretary_by_email(self, session: Session, id:uuid.UUID ) -> SecretaryTable :
        query = session.query(SecretaryTable).filter(SecretaryTable.entity_id == id)

        result = query.scalar()

        return result