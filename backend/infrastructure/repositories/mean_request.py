from sqlalchemy.orm import Session
from sqlalchemy import select, and_, delete
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.mean import MeanPaginationService
from backend.domain.models.tables import TeacherTable, MeanTable
from .base import IRepository
from backend.domain.models.tables import teacher_request_mean_table

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

    def get_by_id(self, teacher_id: str, mean_id:str ) -> None :
        query = select(teacher_request_mean_table)
        query = query.where(
            and_(
                teacher_request_mean_table.c.teacher_id == teacher_id,
                teacher_request_mean_table.c.mean_id == mean_id
            )
        )
        return self.session.execute(query).first()
        

    def delete(self, entity: None, mean_request  ) -> None :
        stmt = delete(teacher_request_mean_table).where(
            and_(
                teacher_request_mean_table.c.teacher_id == mean_request.teacher_id,
                teacher_request_mean_table.c.mean_id == mean_request.mean_id,
            )
        )
        self.session.execute(stmt)
        self.session.commit()
