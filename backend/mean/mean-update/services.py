from sqlalchemy.orm import Session
from sqlalchemy import update
from .filters import ChangeRequest
import uuid 
from database.tables import MeanTable
from mean.mean_common.schemas import  MeanModel

class MeanUpdateService :
    def update_one(self, session : Session , changes : ChangeRequest , mean : MeanModel ) -> MeanModel: 
        query = update(MeanTable).where(MeanTable.entity_id == mean.id)
        
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        session.execute(query)
        session.commit()
        
        mean = mean.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return mean

class MeanListingService :
    def get_mean_by_id(self, session: Session, id : int) -> MeanTable :
        query = session.query(MeanTable).filter(MeanTable.entity_id == id)

        result = query.first()

        return result