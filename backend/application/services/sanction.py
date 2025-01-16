from sqlalchemy.orm import Session
from backend.domain.models.tables import SanctionTable
from backend.domain.schemas.sanction import SanctionCreateModel
from backend.application.services.teacher import TeacherPaginationService



class SanctionCreateService : 
    def create_sanction(self, session: Session , sanction: SanctionCreateModel) -> SanctionTable :
        teacher_pagination_service = TeacherPaginationService()
        teacher = teacher_pagination_service.get_teacher_by_id(session=session, id=sanction.teacher_id)

        new_sanction = SanctionTable(**sanction.model_dump(exclude_unset=True, exclude_none=True))
        new_sanction.teacher = teacher
        teacher.sanctions.append(new_sanction)
        teacher.salary -= sanction.amount
        session.add(new_sanction)
        session.commit()
        return new_sanction