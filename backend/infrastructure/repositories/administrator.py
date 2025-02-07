from sqlalchemy.orm import Session
from backend.domain.schemas.administrador import AdministratorCreateModel, AdministratorModel
from backend.domain.filters.administrador import AdministratorChangeRequest, AdministratorFilterSchema, AdministratorFilterSet
from backend.domain.models.tables import AdministratorTable
from sqlalchemy.orm import Session
from sqlalchemy import update, select
import uuid
from backend.application.utils.auth import get_password_hash, get_password
from .base import IRepository

"""
Repository class for handling administrator-related database operations.
Implements the base repository interface for administrator management.
"""

class AdministratorRepository(IRepository[AdministratorCreateModel,AdministratorModel, AdministratorChangeRequest,AdministratorFilterSchema]):
    """
    Repository for managing administrators in the database.
    Extends IRepository with specific implementations for administrator operations.
    """
    def __init__(self, session):
        """Initialize repository with database session."""
        super().__init__(session)

    def create(self, entity: AdministratorCreateModel) -> AdministratorTable:
        """
        Create a new administrator in the database.
        Args:
            entity: AdministratorCreateModel containing administrator details
        Returns:
            Created AdministratorTable instance with hashed password
        """
        administrator_dict = entity.model_dump(exclude={'password'})
        hashed_password = get_password_hash(get_password(entity))
        new_administrator = AdministratorTable(**administrator_dict, hashed_password=hashed_password)
        self.session.add(new_administrator)
        self.session.commit()
        return new_administrator
    
    def delete(self, entity: AdministratorModel) -> None:
        """
        Delete an administrator from the database.
        Args:
            entity: AdministratorModel to be deleted
        """
        self.session.delete(entity)
        self.session.commit()

    def update(self, changes: AdministratorChangeRequest, entity: AdministratorModel) -> AdministratorModel:
        """
        Update an administrator's information.
        Args:
            changes: AdministratorChangeRequest containing fields to update
            entity: Current AdministratorModel to be updated
        Returns:
            Updated AdministratorModel instance
        """
        table_entity = self.get_by_id(id=entity.id)
        for key, value in changes.model_dump(exclude_unset=True, exclude_none=True).items():
            setattr(table_entity, key, value)
        self.session.commit()

        return entity
    
    def get(self, filter_params: AdministratorFilterSchema) -> list[AdministratorTable]:
        """
        Retrieve administrators based on filter parameters.
        Args:
            filter_params: Filter criteria for administrators
        Returns:
            List of matching AdministratorTable instances
        """
        query = select(AdministratorTable)
        filter_set = AdministratorFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return self.session.execute(query).scalars().all()
    
    def get_by_id(self, id: str) -> AdministratorTable:
        """
        Retrieve an administrator by their ID.
        Args:
            id: String identifier of the administrator
        Returns:
            Matching AdministratorTable instance or None
        """
        query = self.session.query(AdministratorTable).filter(AdministratorTable.entity_id == id)
        result = query.scalar()
        return result
    
    def get_by_email(self, email: str) -> AdministratorTable:
        """
        Retrieve an administrator by their email address.
        Args:
            email: Email address of the administrator
        Returns:
            Matching AdministratorTable instance or None
        """
        query = self.session.query(AdministratorTable).filter(AdministratorTable.email == email)
        result = query.scalar()
        return result
    



   
