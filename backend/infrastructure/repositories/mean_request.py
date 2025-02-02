from sqlalchemy.orm import Session
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.mean import MeanPaginationService
from backend.domain.models.tables import TeacherTable, MeanTable
from .base import IRepository

class MeanRequestRepository(IRepository[None,None, None,None]):
    def __init__(self, session):
        super().__init__(session)

    def create(self, mean : MeanTable, teacher: TeacherTable):
        teacher.mean_request.append(mean)
      
        self.session.commit()
        
        return mean.id
    
    def get(self, filter_params: None) -> list[None] :
        pass

    def update(self, changes : None , entity : None) -> None:
        pass

    def get_by_id(self, id: str ) -> None :
        pass

    def delete(self, entity: None) -> None :
        pass
