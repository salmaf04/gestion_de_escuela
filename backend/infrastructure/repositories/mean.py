from sqlalchemy.orm import Session
from backend.domain.schemas.mean import MeanCreateModel, MeanModel
from backend.domain.models.tables import MeanTable , TechnologicalMeanTable , TeachingMaterialTable, OthersTable, MeanMaintenanceTable, teacher_request_mean_table
from sqlalchemy import and_
import uuid
from sqlalchemy import select, update, and_
from backend.domain.filters.mean import MeanFilterSet , MeanFilterSchema, MeanChangeRequest
from backend.application.services.classroom import ClassroomPaginationService
from fastapi import HTTPException, status
from .base import IRepository

"""
Repository class for handling mean/resource-related database operations.
Implements the base repository interface for managing different types of means (technological, teaching materials, others).
"""

class MeanRepository(IRepository[MeanCreateModel,MeanModel, MeanChangeRequest,MeanFilterSchema]):
    """
    Repository for managing means/resources in the database.
    Extends IRepository with specific implementations for mean operations.
    """
    def __init__(self, session):
        """Initialize repository with database session."""
        super().__init__(session)

    def create(self, entity: MeanCreateModel) -> MeanTable:
        """
        Create a new mean/resource in the database.
        Handles different types of means (technological, teaching material, other).
        Args:
            entity: MeanCreateModel containing mean details including type and classroom
        Returns:
            Created MeanTable instance
        Raises:
            HTTPException: If an invalid mean type is provided
        """
        table_to_insert = {
            "technological_mean": TechnologicalMeanTable,
            "teaching_material": TeachingMaterialTable,
            "other": OthersTable,
        }
        
        classroom_pagination_service = ClassroomPaginationService()
        classroom = classroom_pagination_service.get_classroom_by_id(session=self.session, id=entity.classroom_id)

        mean_dict = entity.model_dump()
        mean_type = table_to_insert.get(entity.type, None)
    
        if mean_type is None:
            mean_valid_types = ', '.join(table_to_insert.keys())
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Inserte un tipo de medio válido : {mean_valid_types}"
            )

        new_mean = mean_type(**mean_dict)
        new_mean.classroom_id = classroom.entity_id
        new_mean.classroom = classroom
        self.session.add(new_mean)
        self.session.commit()
        return new_mean

    def delete(self, entity: MeanModel) -> None:
        """
        Delete a mean/resource from the database.
        Args:
            entity: MeanModel to be deleted
        """
        self.session.delete(entity)
        self.session.commit()
        
    def update(self, changes: MeanChangeRequest, entity: MeanModel) -> MeanModel:
        """
        Update a mean's information.
        Args:
            changes: MeanChangeRequest containing fields to update
            entity: Current MeanModel to be updated
        Returns:
            Updated MeanModel instance
        """
        query = update(MeanTable).where(MeanTable.entity_id == entity.id)
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        self.session.execute(query)
        self.session.commit()
        
        mean = entity.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return mean
        
    def get_by_id(self, id: str) -> MeanTable:
        """
        Retrieve a mean by its ID.
        Args:
            id: String identifier of the mean
        Returns:
            Matching MeanTable instance or None
        """
        query = self.session.query(MeanTable).filter(MeanTable.entity_id == id)
        result = query.scalar()
        return result
    
    def get(self, filter_params: MeanFilterSchema) -> list[MeanTable]:
        """
        Retrieve means based on filter parameters.
        Args:
            filter_params: Filter criteria for means
        Returns:
            List of matching MeanTable instances
        """
        query = select(MeanTable, teacher_request_mean_table)
        query = query.outerjoin(teacher_request_mean_table, MeanTable.entity_id == teacher_request_mean_table.c.mean_id)
        filter_set = MeanFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return self.session.execute(query).all()
    
    def get_avaliable_means(self) -> list[MeanTable]:
        """
        Get all available means that are:
        - Not marked for replacement
        - Not currently requested by teachers
        - Not under maintenance
        Returns:
            List of available MeanTable instances
        """
        query = select(MeanTable)
        query = query.where(and_(
            MeanTable.to_be_replaced == False,
            MeanTable.entity_id.notin_(
                select(teacher_request_mean_table.c.mean_id)),
            MeanTable.entity_id.notin_(
                select(MeanMaintenanceTable.mean_id).where(MeanMaintenanceTable.finished == False)
            ))
        )
        return self.session.execute(query).scalars().all()
