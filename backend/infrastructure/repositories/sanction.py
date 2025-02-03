from sqlalchemy.orm import Session
from backend.domain.models.tables import SanctionTable
from backend.domain.schemas.sanction import SanctionCreateModel
from backend.domain.schemas.teacher import TeacherModel
from backend.application.services.teacher import TeacherPaginationService
from . base import IRepository

"""
Repository class for handling teacher sanction-related database operations.
Implements the base repository interface for managing disciplinary sanctions.
"""

class SanctionRepository(IRepository[SanctionCreateModel,SanctionTable, None,None]):
    """
    Repository for managing teacher sanctions in the database.
    Extends IRepository with specific implementations for sanction operations.
    """
    def __init__(self, session):
        """Initialize repository with database session."""
        super().__init__(session)

    def create(self, entity: SanctionCreateModel, teacher: TeacherModel) -> SanctionTable:
        """
        Create a new sanction record and update teacher's salary.
        Args:
            entity: SanctionCreateModel containing sanction details
            teacher: TeacherModel instance receiving the sanction
        Returns:
            Created SanctionTable instance
        Note:
            This method also reduces the teacher's salary by the sanction amount
        """
        new_sanction = SanctionTable(**entity.model_dump(exclude_unset=True, exclude_none=True))
        new_sanction.teacher = teacher
        teacher.sanctions.append(new_sanction)
        teacher.salary -= entity.amount
        self.session.add(new_sanction)
        self.session.commit()
        return new_sanction
    
    def get(self, filter_params: None) -> list[SanctionTable]:
        """Get sanctions - Not implemented."""
        pass

    def update(self, changes: None, entity: SanctionTable) -> SanctionTable:
        """Update sanction - Not implemented."""
        pass

    def get_by_id(self, id: str) -> SanctionTable:
        """Get sanction by ID - Not implemented."""
        pass

    def delete(self, entity: SanctionTable) -> None:
        """Delete sanction - Not implemented."""    
        pass

