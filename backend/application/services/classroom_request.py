from sqlalchemy.orm import Session
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.classroom import ClassroomPaginationService
from backend.domain.models.tables import TeacherTable, ClassroomTable
from backend.infrastructure.repositories.classroom_request import ClassroomRequestRepository


class ClassroomRequestCreateService :
    def __init__(self, session):
        self.session = session
        self.repo_instance = ClassroomRequestRepository(session)
        self.teacher_pagination_service = TeacherPaginationService(session)
        self.classroom_pagination_service = ClassroomPaginationService(session)

    def create_classroom_request(self, teacher_id : str, classroom_id : str) :
        teacher = self.teacher_pagination_service.get_teacher_by_id(id=teacher_id)
        classroom = self.classroom_pagination_service.get_classroom_by_id(id=classroom_id)
        return self.repo_instance.create(teacher, classroom)

class ClassroomRequestPaginationService :
    def __init__(self, session) :
        self.repo_instance = ClassroomRequestRepository(session)

    def get_by_id(self, teacher_id: str, classroom_id : str ) :
        return self.repo_instance.get_by_id(teacher_id=teacher_id, classroom_id=classroom_id)

class ClassroomRequestDeletionService :
    def __init__(self, session) :
        self.repo_instance = ClassroomRequestRepository(session)

    def delete(self, classroom_request ) :
        return self.repo_instance.delete(entity=None, classroom_request=classroom_request)
