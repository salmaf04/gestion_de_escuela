from sqlalchemy.orm import Session
from backend.domain.schemas.valoration_period import ValorationPeriodChangeRequest
from backend.domain.models.tables import ValorationPeriodTable
from sqlalchemy import update, insert
from backend.infrastructure.repositories.valoration_period import ValorationPeriodRepository

"""
This module defines a service for updating valoration period records.

Classes:
    ValorationPeriodUpdateService: A service for updating valoration period records.

Class Details:

ValorationPeriodUpdateService:
    - This service is responsible for updating valoration period records.
    - It utilizes the ValorationPeriodRepository to interact with the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - update_one(changes: ValorationPeriodChangeRequest): 
            Updates a valoration period record with the provided changes using the ValorationPeriodChangeRequest.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - ValorationPeriodRepository for database operations related to valoration periods.
    - ValorationPeriodChangeRequest and ValorationPeriodTable for data representation.
"""

class ValorationPeriodUpdateService :
    def __init__(self, session):
        self.repo_instance = ValorationPeriodRepository(session)

    def update_one(self, changes : ValorationPeriodChangeRequest) :
        return self.repo_instance.update(changes)
    
class ValorationPeriodPaginationService :
    def __init__(self, session):
        self.repo_instance = ValorationPeriodRepository(session)

    def get_valoration_period(self, filter_params: None) -> list[ValorationPeriodTable] :
        return self.repo_instance.get(filter_params)