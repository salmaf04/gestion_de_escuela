from administrator.administrator_common.schemas import AdministratorModel
from sqlalchemy.orm import Session
from database.tables import AdministratorTable
import uuid

class AdministratorDeletionService:
    def delete_administrator(self, session: Session, administrator: AdministratorModel) -> None :
        session.delete(administrator)
        session.commit()

class AdministratorPaginationService :
    def get_administrator_by_email(self, session: Session, id:uuid.UUID ) -> AdministratorTable :
        query = session.query(AdministratorTable).filter(AdministratorTable.entity_id == id)

        result = query.scalar()

        return result