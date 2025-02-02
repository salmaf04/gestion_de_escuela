from sqlalchemy.orm import Session
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.mean import MeanPaginationService
from .. import IRepository

class MeanRequestRepository(IRepository[None,None, None,None]):
    def __init__(self, session):
        super().__init__(session)

    def create(self, entity: None, mean_id : str, teacher_id: str):
        teacher_pagination = TeacherPaginationService()
        mean_pagination = MeanPaginationService()

        teacher = teacher_pagination.get_teacher_by_id(session=self.session, id=teacher_id)
        mean = mean_pagination.get_mean_by_id(session=self.session, id=mean_id)

        teacher.mean_request.append(mean)
      
        self.session.commit()
        
        return mean_id
