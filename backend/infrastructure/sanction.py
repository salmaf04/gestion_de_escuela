from sqlalchemy.orm import Session
from backend.domain.models.tables import SanctionTable
from backend.domain.schemas.sanction import SanctionCreateModel
from backend.application.services.teacher import TeacherPaginationService
from .. import IRepository

class SanctionRepository(IRepository[SanctionCreateModel,SanctionTable, None,None]):
    def __init__(self, session):
        super().__init__(session)

    def create(self, entity: SanctionCreateModel) -> SanctionTable :
        teacher_pagination_service = TeacherPaginationService()
        teacher = teacher_pagination_service.get_teacher_by_id(session=self.session, id=entity.teacher_id)

        new_sanction = SanctionTable(**entity.model_dump(exclude_unset=True, exclude_none=True))
        new_sanction.teacher = teacher
        teacher.sanctions.append(new_sanction)
        teacher.salary -= entity.amount
        self.session.add(new_sanction)
        self.session.commit()
        return new_sanction

