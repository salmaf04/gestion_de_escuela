from sqlalchemy.orm import Session
from .schemas import MeanCreateModel, MeanModel
from database.tables import MeanTable
from sqlalchemy import and_

class MeanCreateService() :

    def mean_create(self, session: Session, mean: MeanCreateModel) -> MeanTable :
        mean_dict = mean.model_dump()

        new_mean = MeanTable(**mean_dict)
        session.add(new_mean)
        session.commit()
        return new_mean
    

  
