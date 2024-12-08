from sqlalchemy.orm import Session
from backend.domain.schemas.mean import MeanCreateModel, MeanModel
from backend.domain.models.tables import MeanTable
from sqlalchemy import and_
import uuid
from sqlalchemy import select, update
from backend.domain.filters.mean import MeanFilterSet , MeanFilterSchema, ChangeRequest

class MeanCreateService() :

    def mean_create(self, session: Session, mean: MeanCreateModel) -> MeanTable :
        mean_dict = mean.model_dump()

        new_mean = MeanTable(**mean_dict)
        session.add(new_mean)
        session.commit()
        return new_mean
    
class MeanDeletionService:
    def delete_mean(self, session: Session, mean: MeanModel) -> None :
        session.delete(mean)
        session.commit()
        
        
class MeanUpdateService :
    def update_one(self, session : Session , changes : ChangeRequest , mean : MeanModel ) -> MeanModel: 
        query = update(MeanTable).where(MeanTable.entity_id == mean.id)
        
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        session.execute(query)
        session.commit()
        
        mean = mean.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return mean
    

class MeanPaginationService :
    def get_mean_by_id(self, session: Session, id:uuid.UUID ) -> MeanTable :
        query = session.query(MeanTable).filter(MeanTable.entity_id == id)

        result = query.scalar()

        return result
    
    def get_means(self, session: Session, filter_params: MeanFilterSchema) -> list[MeanTable] :
        query = select(MeanTable)
        filter_set = MeanFilterSet(session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return session.execute(query).scalars().all()
    

  
