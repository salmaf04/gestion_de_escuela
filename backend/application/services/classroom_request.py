from sqlalchemy.orm import Session
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.classroom import ClassroomPaginationService



class ClassroomRequestCreateService :
    def create_classroom_request(self, session: Session, classroom_id: str, teacher_id: str) :
        teacher_pagination = TeacherPaginationService()
        classroom_pagination = ClassroomPaginationService()

        teacher = teacher_pagination.get_teacher_by_id(session=session, id=teacher_id)
        classroom = classroom_pagination.get_classroom_by_id(session=session, id=classroom_id)

        teacher.classroom_request.append(classroom)
      
        session.commit()
        
        return classroom_id
