from sqlalchemy.orm import Session
from backend.domain.models.tables import SanctionTable
from backend.domain.schemas.sanction import SanctionCreateModel
from backend.domain.schemas.teacher import TeacherModel
from backend.application.services.teacher import TeacherPaginationService
from . base import IRepository

class SanctionRepository(IRepository[SanctionCreateModel,SanctionTable, None,None]):
    def __init__(self, session):
        super().__init__(session)

    def create(self, entity: SanctionCreateModel, teacher : TeacherModel) -> SanctionTable :
        new_sanction = SanctionTable(**entity.model_dump(exclude_unset=True, exclude_none=True))
        new_sanction.teacher = teacher
        teacher.sanctions.append(new_sanction)
        teacher.salary -= entity.amount
        self.session.add(new_sanction)
        self.session.commit()
        return new_sanction
    
    def get(self, filter_params: None) -> list[SanctionTable] :
        pass

    def update(self, changes : None , entity : SanctionTable) -> SanctionTable:
        pass

    def get_by_id(self, id: str ) -> SanctionTable :
        pass

    def delete(self, entity: SanctionTable) -> None :    
        pass

