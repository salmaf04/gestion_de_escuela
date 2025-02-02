from sqlalchemy.orm import Session
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.classroom import ClassroomPaginationService
from .. import IRepository

class ClassroomRequestRepository(IRepository[None,None, None,None]):
    def __init__(self, session):
        super().__init__(session)

    def create(self, entity: None, classroom_id : str, teacher_id: str):
        teacher_pagination = TeacherPaginationService()
        classroom_pagination = ClassroomPaginationService()

        teacher = teacher_pagination.get_teacher_by_id(session=self.session, id=teacher_id)
        classroom = classroom_pagination.get_classroom_by_id(session=self.session, id=classroom_id)

        teacher.classroom_request.append(classroom)
      
        self.session.commit()
        
        return classroom_id

