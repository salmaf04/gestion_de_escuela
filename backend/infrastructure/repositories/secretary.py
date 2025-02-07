from sqlalchemy.orm import Session
from backend.domain.schemas.secretary import SecretaryCreateModel, SecretaryModel
from backend.domain.models.tables import SecretaryTable
import uuid
from sqlalchemy import update, select
from backend.domain.filters.secretary import SecretaryChangeRequest, SecretaryFilterSchema, SecretaryFilterSet
from backend.application.utils.auth import get_password_hash, get_password
from .base import IRepository

"""
Repository class for handling secretary-related database operations.
Implements the base repository interface for managing secretary records.
"""

class SecretaryRepository(IRepository[SecretaryCreateModel,SecretaryModel, SecretaryChangeRequest,SecretaryFilterSchema]):
    """
    Repository for managing secretaries in the database.
    Extends IRepository with specific implementations for secretary operations.
    """
    def __init__(self, session):
        """Initialize repository with database session."""
        super().__init__(session)

    def create(self, entity: SecretaryCreateModel) -> SecretaryTable:
        """
        Create a new secretary record with hashed password.
        Args:
            entity: SecretaryCreateModel containing secretary details
        Returns:
            Created SecretaryTable instance
        """
        secretary_dict = entity.model_dump(exclude={'password'})
        hashed_password = get_password_hash(get_password(entity))
        new_secretary = SecretaryTable(**secretary_dict, hashed_password=hashed_password)
        self.session.add(new_secretary)
        self.session.commit()
        return new_secretary

    def delete(self, entity: SecretaryModel) -> None:
        """
        Delete a secretary from the database.
        Args:
            entity: SecretaryModel instance to be deleted
        """
        self.session.delete(entity)
        self.session.commit()

    def update(self, changes: SecretaryChangeRequest, entity: SecretaryModel) -> SecretaryModel:
        """
        Update a secretary's information.
        Args:
            changes: SecretaryChangeRequest containing fields to update
            entity: Current SecretaryModel to be updated
        Returns:
            Updated SecretaryModel instance
        """
        table_entity = self.get_by_id(id=entity.id)
        for key, value in changes.model_dump(exclude_unset=True, exclude_none=True).items():
            setattr(table_entity, key, value)
        self.session.commit()

        return entity
    
    def get_by_id(self, id: str) -> SecretaryTable:
        """
        Retrieve a secretary by their ID.
        Args:
            id: String identifier of the secretary
        Returns:
            Matching SecretaryTable instance or None
        """
        query = self.session.query(SecretaryTable).filter(SecretaryTable.entity_id == id)
        result = query.scalar()
        return result
    
    def get(self, filter_params: SecretaryFilterSchema) -> list[SecretaryTable]:
        """
        Retrieve secretaries based on filter parameters.
        Args:
            filter_params: Filter criteria for secretaries
        Returns:
            List of matching SecretaryTable instances
        """
        query = select(SecretaryTable)
        filter_set = SecretaryFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return self.session.execute(query).scalars().all()

    def get_secretary_by_email(self, email: str) -> SecretaryTable:
        """
        Retrieve a secretary by their email address.
        Args:
            email: Email address of the secretary
        Returns:
            Matching SecretaryTable instance or None
        """
        query = self.session.query(SecretaryTable).filter(SecretaryTable.email == email)
        result = query.first()
        return result
    