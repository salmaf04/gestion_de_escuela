from sqlalchemy.orm import Session
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.mean import MeanPaginationService
from backend.infrastructure.repositories.mean_request import MeanRequestRepository

class MeanRequestCreateService :
    def __init__(self, session):
        self.repo_instance = MeanRequestRepository(session)
        self.teacher_pagination_service = TeacherPaginationService(session)
        self.mean_pagination_service = MeanPaginationService(session)

    def create_mean_request(self, mean_id: str, teacher_id: str) :
        mean = self.mean_pagination_service.get_mean_by_id(id=mean_id)
        teacher = self.teacher_pagination_service.get_teacher_by_id(id=teacher_id)
        return self.repo_instance.create(mean=mean, teacher=teacher)
    
class MeanRequestPaginationService :
    def __init__(self, session) :
        self.repo_instance = MeanRequestRepository(session)

    def get_by_id(self, teacher_id: str, mean_id: str ) :
        return self.repo_instance.get_by_id(teacher_id=teacher_id, mean_id=mean_id)

class MeanRequestDeletionService :
    def __init__(self, session) :
        self.repo_instance = MeanRequestRepository(session)

    def delete(self, mean_request ) :
        return self.repo_instance.delete(entity=None, mean_request=mean_request)
