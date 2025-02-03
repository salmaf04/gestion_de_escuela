from sqlalchemy.orm import Session
from backend.domain.schemas.valoration_period import ValorationPeriodChangeRequest
from backend.domain.models.tables import ValorationPeriodTable
from sqlalchemy import update, insert
from backend.infrastructure.repositories.valoration_period import ValorationPeriodRepository

class ValorationPeriodUpdateService :
    def __init__(self, session):
        self.repo_instance = ValorationPeriodRepository(session)

    def update_one(self, changes : ValorationPeriodChangeRequest) :
        return self.repo_instance.update(changes)