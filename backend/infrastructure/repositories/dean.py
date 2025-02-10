from sqlalchemy.orm import Session
from backend.domain.schemas.dean import DeanCreateModel, DeanModel
from backend.domain.models.tables import DeanTable, UserTable
from sqlalchemy import and_, update
import uuid
from sqlalchemy import select, delete
from backend.domain.filters.dean import DeanFilterSet , DeanFilterSchema, DeanChangeRequest
from backend.application.utils.auth import get_password_hash, get_password
from .base import IRepository

"""
Repository class for handling dean-related database operations.
Implements the base repository interface for dean management.
"""

class DeanRepository(IRepository[DeanCreateModel, DeanModel, DeanChangeRequest, DeanFilterSchema]):
    """
    Repository for managing deans in the database.
    Extends IRepository with specific implementations for dean operations.
    """
    def __init__(self, session):
        """Initialize repository with database session."""
        super().__init__(session)

    def create(self, entity: DeanCreateModel) -> DeanTable:
        """
        Create a new dean in the database with hashed password.
        Args:
            entity: DeanCreateModel containing dean details
        Returns:
            Created DeanTable instance
        """
        dean_dict = entity.model_dump(exclude={'password'})
        hashed_password = get_password_hash(get_password(entity))
        new_dean = DeanTable(**dean_dict, hashed_password=hashed_password)
        self.session.add(new_dean)
        self.session.commit()
        return new_dean
    
    def delete(self, entity: DeanModel) -> None :
        delete_statement = delete(DeanTable).where(DeanTable.entity_id == entity.id)
        update_type = update(UserTable).where(UserTable.entity_id == entity.id).values(type="teacher")
        self.session.execute(update_type)
        self.session.commit()
        self.session.execute(delete_statement)
        self.session.commit()

    def update(self, changes : DeanChangeRequest , entity : DeanModel) -> DeanModel:
        table_entity = self.get_by_id(id=entity.id)
        for key, value in changes.model_dump(exclude_unset=True, exclude_none=True).items():
            setattr(table_entity, key, value)
        self.session.commit()

        return entity
        
    def get_by_id(self, id: str ) -> DeanTable :    
        query = self.session.query(DeanTable).filter(DeanTable.entity_id == id)
        result = query.scalar() 
        return result
    
    def get(self, filter_params: DeanFilterSchema) -> list[DeanTable] :
        query = select(DeanTable)
        filter_set = DeanFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return self.session.execute(query).scalars().all()

    def get_by_email(self, email: str) -> DeanTable :
        query = self.session.query(DeanTable).filter(DeanTable.email == email)

        result = query.first()

        return result
    
 