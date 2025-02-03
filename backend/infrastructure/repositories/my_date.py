from sqlalchemy.orm import Session
from backend.domain.schemas.my_date import DateCreateModel
from backend.domain.models.tables import MyDateTable
import uuid
from .base import IRepository

"""
Repository class for handling date-related database operations.
Implements the base repository interface for managing date records.
"""

class DateRepository(IRepository[DateCreateModel,MyDateTable, None,None]):
    """
    Repository for managing dates in the database.
    Extends IRepository with specific implementations for date operations.
    """
    def __init__(self, session):
        """Initialize repository with database session."""    
        super().__init__(session)

    def create(self, entity: DateCreateModel) -> MyDateTable:
        """
        Create a new date record in the database.
        Args:
            entity: DateCreateModel containing date details
        Returns:
            Created MyDateTable instance
        """
        date_dict = entity.model_dump()
        new_date = MyDateTable(**date_dict)
        self.session.add(new_date)
        self.session.commit()
        return new_date
    
    def get_by_id(self, id: str) -> MyDateTable:
        """
        Retrieve a date record by its ID.
        Args:
            id: String identifier of the date record
        Returns:
            Matching MyDateTable instance or None
        """
        query = self.session.query(MyDateTable).filter(MyDateTable.entity_id == id)
        result = query.scalar()
        return result

    # Unimplemented interface methods
    def get(self, filter_params: None) -> list[MyDateTable]:
        """Get date records - Not implemented."""
        pass

    def update(self, changes: None, entity: MyDateTable) -> MyDateTable:
        """Update date record - Not implemented."""
        pass

    def delete(self, entity: MyDateTable) -> None:
        """Delete date record - Not implemented."""
        pass

    def get_by_id(self, id: str ) -> MyDateTable :
        query = self.session.query(MyDateTable).filter(MyDateTable.entity_id == id)

        result = query.scalar()

        return result

