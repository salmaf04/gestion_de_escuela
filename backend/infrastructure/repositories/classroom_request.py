from sqlalchemy.orm import Session
from sqlalchemy import select, and_, delete
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.classroom import ClassroomPaginationService
from .base import IRepository
from backend.domain.models.tables import TeacherTable, ClassroomTable, teacher_request_classroom_table

"""
Repository class for handling classroom request operations between teachers and classrooms.
Implements the base repository interface for managing teacher-classroom associations.
"""

class ClassroomRequestRepository(IRepository[None,None, None,None]):
    """
    Repository for managing classroom requests in the database.
    Handles the many-to-many relationship between teachers and classrooms.
    """
    def __init__(self, session):
        """Initialize repository with database session."""
        super().__init__(session)

    def create(self, teacher: TeacherTable, classroom: ClassroomTable):
        """
        Create a new classroom request association.
        Args:
            teacher: TeacherTable instance making the request
            classroom: ClassroomTable instance being requested
        Returns:
            UUID of the requested classroom
        """
        teacher.classroom_request.append(classroom)
        self.session.commit()
        return classroom.entity_id
    
    def get(self, filter_params: None) -> list[None]:
        """Get classroom requests - Not implemented."""
        pass

    def update(self, changes: None, entity: None) -> None:
        """Update classroom request - Not implemented."""
        pass

    def get_by_id(self, teacher_id: str, classroom_id: str) -> None:
        """
        Check if a specific teacher-classroom request exists.
        Args:
            teacher_id: ID of the teacher
            classroom_id: ID of the classroom
        Returns:
            First matching record or None
        """
        query = select(teacher_request_classroom_table)
        query = query.where(
            and_(
                teacher_request_classroom_table.c.teacher_id == teacher_id,
                teacher_request_classroom_table.c.classroom_id == classroom_id
            )
        )
        return self.session.execute(query).first()
        
    def delete(self, entity: None, classroom_request) -> None:
        """
        Delete a classroom request association.
        Args:
            entity: Not used (maintained for interface compatibility)
            classroom_request: Object containing teacher_id and classroom_id
        """
        stmt = delete(teacher_request_classroom_table).where(
            and_(
                teacher_request_classroom_table.c.teacher_id == classroom_request.teacher_id,
                teacher_request_classroom_table.c.classroom_id == classroom_request.classroom_id,
            )
        )
        self.session.execute(stmt)
        self.session.commit()
