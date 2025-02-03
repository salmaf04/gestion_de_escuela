"""
Repository class for handling mean/resource request operations.
Manages the many-to-many relationship between teachers and means/resources.
"""

from sqlalchemy.orm import Session
from sqlalchemy import select, and_, delete
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.mean import MeanPaginationService
from backend.domain.models.tables import TeacherTable, MeanTable
from .base import IRepository
from backend.domain.models.tables import teacher_request_mean_table

class MeanRequestRepository(IRepository[None,None, None,None]):
    """
    Repository for managing resource requests in the database.
    Handles teacher requests for specific means/resources.
    """
    def __init__(self, session):
        """Initialize repository with database session."""
        super().__init__(session)

    def create(self, mean: MeanTable, teacher: TeacherTable):
        """
        Create a new mean request association.
        Args:
            mean: MeanTable instance being requested
            teacher: TeacherTable instance making the request
        Returns:
            ID of the requested mean
        """
        teacher.mean_request.append(mean)
        self.session.commit()
        return mean.id
    
    def get(self, filter_params: None) -> list[None] :
        pass

    def update(self, changes : None , entity : None) -> None:
        pass

    def get_by_id(self, teacher_id: str, mean_id:str ) -> None :
        """
        Check if a specific teacher-mean request exists.
        Args:
            teacher_id: ID of the teacher
            mean_id: ID of the requested mean
        Returns:
            First matching record or None
        """
        query = select(teacher_request_mean_table)
        query = query.where(
            and_(
                teacher_request_mean_table.c.teacher_id == teacher_id,
                teacher_request_mean_table.c.mean_id == mean_id
            )
        )
        return self.session.execute(query).first()
        
    def delete(self, entity: None, mean_request) -> None:
        """
        Delete a mean request association.
        Args:
            entity: Not used (maintained for interface compatibility)
            mean_request: Object containing teacher_id and mean_id
        """
        stmt = delete(teacher_request_mean_table).where(
            and_(
                teacher_request_mean_table.c.teacher_id == mean_request.teacher_id,
                teacher_request_mean_table.c.mean_id == mean_request.mean_id,
            )
        )
        self.session.execute(stmt)
        self.session.commit()
