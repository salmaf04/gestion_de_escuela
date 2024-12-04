from mean.mean_common.schemas import MeanModel
from sqlalchemy.orm import Session
from database.tables import MeanTable
import uuid

class MeanDeletionService:
    def delete_mean(self, session: Session, mean: MeanModel) -> None :
        session.delete(mean)
        session.commit()

class MeanPaginationService :
    def get_mean_by_id(self, session: Session, id:uuid.UUID ) -> MeanTable :
        query = session.query(MeanTable).filter(MeanTable.entity_id == id)

        result = query.scalar()

        return result