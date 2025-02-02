from sqlalchemy.orm import Session
from backend.domain.schemas.valoration_period import ValorationPeriodChangeRequest
from backend.domain.models.tables import ValorationPeriodTable
from sqlalchemy import update, insert
from .base import IRepository

class ValorationPeriodRepository(IRepository[ValorationPeriodChangeRequest,ValorationPeriodTable, None,None]):
    def __init__(self, session):
        super().__init__(session)

    def update(self, changes : ValorationPeriodChangeRequest) :
        period = self.session.query(ValorationPeriodTable).first()

        period.open = changes.open
        self.session.commit()

    def create(self, entity: ValorationPeriodChangeRequest) -> ValorationPeriodTable :
        pass

    def delete(self, entity: ValorationPeriodTable) -> None :
        pass

    def get(self, filter_params: None) -> list[ValorationPeriodTable] :
        pass

    def get_by_id(self, id: str ) -> ValorationPeriodTable :
        pass