from sqlalchemy.orm import Session
from backend.domain.models.tables import SanctionTable
from backend.domain.schemas.sanction import SanctionCreateModel
from backend.application.services.teacher import TeacherPaginationService
from backend.infrastructure.repositories.sanction import SanctionRepository

class SanctionCreateService : 
    def __init__(self, session):
        self.repo_instance = SanctionRepository(session)
        self.teacher_pagination_service = TeacherPaginationService(session)

    def create_sanction(self, sanction: SanctionCreateModel) -> SanctionTable :
        teacher = self.teacher_pagination_service.get_teacher_by_id(id=sanction.teacher_id)
        return self.repo_instance.create(sanction, teacher)
