from sqlalchemy.orm import Session
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.mean import MeanPaginationService



class MeanRequestCreateService :
    def create_mean_request(self, session: Session, mean_id: str, teacher_id: str) :
        teacher_pagination = TeacherPaginationService()
        mean_pagination = MeanPaginationService()

        teacher = teacher_pagination.get_teacher_by_id(session=session, id=teacher_id)
        mean = mean_pagination.get_mean_by_id(session=session, id=mean_id)

        teacher.mean_request.append(mean)
      
        session.commit()
        
        return mean_id
