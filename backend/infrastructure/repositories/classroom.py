from backend.domain.schemas.classroom import ClassroomCreateModel, ClassroomModel
from backend.domain.models.tables import ClassroomTable, MeanTable
from sqlalchemy.orm import Session
from backend.domain.filters.classroom import ClassroomFilterSchema, ClassroomFilterSet, ClassroomChangeRequest
from sqlalchemy import select, update
import uuid

from .base import IRepository

"""
Repository class for handling classroom-related database operations.
Implements the base repository interface for classroom management.
"""

class ClassroomRepository(IRepository[ClassroomCreateModel,ClassroomModel, ClassroomChangeRequest,ClassroomFilterSchema]):
    """
    Repository for managing classrooms in the database.
    Extends IRepository with specific implementations for classroom operations.
    """
    def __init__(self, session):
        """Initialize repository with database session."""
        super().__init__(session)

    def create(self, entity: ClassroomCreateModel) -> ClassroomTable:
        """
        Create a new classroom in the database.
        Args:
            entity: ClassroomCreateModel containing classroom details
        Returns:
            Created ClassroomTable instance
        """
        new_classroom = ClassroomTable(**entity.model_dump())
        self.session.add(new_classroom)
        self.session.commit()
        return new_classroom
    
    def delete(self, entity: ClassroomTable) -> None:
        """
        Delete a classroom from the database.
        Args:
            entity: ClassroomTable instance to be deleted
        """
        self.session.delete(entity)
        self.session.commit()

    def update(self, changes: ClassroomChangeRequest, entity: ClassroomModel) -> ClassroomModel:
        """
        Update a classroom's information.
        Args:
            changes: ClassroomChangeRequest containing fields to update
            entity: Current ClassroomModel to be updated
        Returns:
            Updated ClassroomModel instance
        """
        query = update(ClassroomTable).where(ClassroomTable.entity_id == entity.id)
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        self.session.execute(query)
        self.session.commit()
        return entity
    
    def get_by_id(self, id: str) -> ClassroomTable:
        """
        Retrieve a classroom by its ID.
        Args:
            id: String identifier of the classroom
        Returns:
            Matching ClassroomTable instance or None
        """
        query = self.session.query(ClassroomTable)
        query = query.filter(ClassroomTable.entity_id == id)
        return self.session.execute(query).scalars().first()
    
    def get(self, filter_params: ClassroomFilterSchema) -> list[ClassroomTable]:
        """
        Retrieve classrooms based on filter parameters.
        Includes associated means (resources) through outer join.
        Args:
            filter_params: Filter criteria for classrooms
        Returns:
            List of matching ClassroomTable instances with their means
        """
        query = select(ClassroomTable, MeanTable)
        query = query.outerjoin(MeanTable, ClassroomTable.entity_id == MeanTable.classroom_id)
        filter_set = ClassroomFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        query = query.group_by(ClassroomTable, MeanTable)
        query = query.order_by(ClassroomTable.entity_id)
        return self.session.execute(query).all()
    
    