from sqlalchemy.orm import Session
from backend.domain.schemas.valoration_period import ValorationPeriodChangeRequest
from backend.domain.models.tables import ValorationPeriodTable
from sqlalchemy import update, insert

class ValorationPeriodUpdateService :
    def update_one(self, session : Session , changes : ValorationPeriodChangeRequest) :
        period = session.query(ValorationPeriodTable).first()

        period.open = changes.open
        session.commit()