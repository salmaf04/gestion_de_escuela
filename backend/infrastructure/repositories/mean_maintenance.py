"""
Repository class for handling maintenance records of means/resources.
Implements complex queries for maintenance statistics and reporting.
"""

from sqlalchemy.orm import Session
from backend.domain.schemas.mean_maintenance import MeanMaintenanceCreateModel, MeanMaintenanceModel
from backend.domain.models.tables import MeanMaintenanceTable
from sqlalchemy import select, update
from backend.application.services.mean import MeanPaginationService
from backend.application.services.my_date import DatePaginationService
from backend.domain.filters.mean_maintenance import MeanMaintenanceFilterSet , MeanMaintenanceFilterSchema,  MeanMaintenanceChangeRequest
from backend.domain.models.tables import MeanMaintenanceTable, TechnologicalMeanTable, MeanTable, ClassroomTable
import uuid
from datetime import datetime, timedelta, timezone
from sqlalchemy import func
from sqlalchemy import extract, and_
from .base import IRepository

class MeanMaintenanceRepository(IRepository[MeanMaintenanceCreateModel,MeanMaintenanceTable, MeanMaintenanceChangeRequest,MeanMaintenanceFilterSchema]):
    """
    Repository for managing maintenance records of means/resources.
    Includes methods for statistical analysis and reporting.
    """
    def __init__(self, session):
        """Initialize repository with database session."""
        super().__init__(session)

    def create(self, entity: MeanMaintenanceCreateModel, mean: MeanTable) -> MeanMaintenanceTable:
        """
        Create a new maintenance record for a specific mean/resource.
        Args:
            entity: MeanMaintenanceCreateModel containing maintenance details
            mean: MeanTable instance that needs maintenance
        Returns:
            Created MeanMaintenanceTable instance
        """
        date_converted = datetime.strptime(entity.date, "%d-%m-%Y")
        mean_maintenance_dict = entity.model_dump(exclude={"date"})
        new_mean_maintenance = MeanMaintenanceTable(**mean_maintenance_dict, date=date_converted)
        mean = mean  
        
        new_mean_maintenance.mean = mean
        mean.mean_maintenance_association.append(new_mean_maintenance)

        self.session.add(new_mean_maintenance)
        self.session.commit()
        return new_mean_maintenance
    
    def delete(self, entity: MeanMaintenanceTable) -> None:
        """
        Delete a maintenance record from the database.
        Args:
            entity: MeanMaintenanceTable instance to be deleted
        """
        self.session.delete(entity)
        self.session.commit()

    def update(self, changes: MeanMaintenanceChangeRequest, entity: MeanMaintenanceModel) -> MeanMaintenanceTable:
        """
        Update a maintenance record's information.
        Args:
            changes: MeanMaintenanceChangeRequest containing fields to update
            entity: Current MeanMaintenanceModel to be updated
        Returns:
            Updated MeanMaintenanceTable instance
        """
        query = update(MeanMaintenanceTable).where(MeanMaintenanceTable.entity_id == entity.id)
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        self.session.execute(query)
        self.session.commit()
        
        mean_maintenance = entity.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return mean_maintenance
    
    def get_by_id(self, id: str) -> MeanMaintenanceTable:
        """
        Retrieve a maintenance record by its ID.
        Args:
            id: String identifier of the maintenance record
        Returns:
            Matching MeanMaintenanceTable instance or None
        """
        query = select(MeanMaintenanceTable).where(MeanMaintenanceTable.entity_id == id)
        result = self.session.execute(query).scalars().first()
        return result

    def get(self, filter_params: MeanMaintenanceFilterSchema) -> list[MeanMaintenanceTable]:
        """
        Retrieve maintenance records based on filter parameters.
        Args:
            filter_params: Filter criteria for maintenance records
        Returns:
            List of matching MeanMaintenanceTable instances
        """
        query = select(MeanMaintenanceTable)
        filter_set = MeanMaintenanceFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True)) 
        return self.session.execute(query).scalars().all()
    
    def get_mainenance_by_classroom(self):
        """
        Get maintenance statistics grouped by classroom and mean type.
        Returns maintenance records from the last 2 years.
        Returns:
            Query results containing classroom, mean type, and maintenance count
        """
        query = select(MeanMaintenanceTable.mean.classroom, MeanMaintenanceTable.mean.type, 
                      func.count(MeanMaintenanceTable.entity_id).label("count"))
        query.where(MeanMaintenanceTable.date == datetime.now(timezone.utc) - timedelta(days=730))
        query.group_by(MeanMaintenanceModel.mean.classroom, MeanMaintenanceModel.mean.type)
        return self.session.execute(query).scalars().all()

    def maintenace_average(self):
        """
        Calculate maintenance cost averages for technological means.
        Focuses on means with more than 2 maintenances in the last year.
        Returns:
            Query results containing mean ID, name, and average maintenance cost
        """
        # Subquery para calcular costos promedio
        average_cost_subquery = (
        select(
            TechnologicalMeanTable.id,
            (func.sum(MeanMaintenanceTable.cost) / func.count(MeanMaintenanceTable.entity_id)).label('average_cost'),
            func.count(MeanMaintenanceTable.mean_id).label('maintenance_count')
        )
        .join(MeanMaintenanceTable, TechnologicalMeanTable.id == MeanMaintenanceTable.mean_id)
        .where(MeanMaintenanceTable.date >= datetime.now(timezone.utc) - timedelta(days=365))
        .group_by(TechnologicalMeanTable.id)
        .having(func.count(MeanMaintenanceTable.mean_id) > 2)  
        .subquery()
    )
    
        query = (
            select(
                TechnologicalMeanTable.id,
                TechnologicalMeanTable.name,
                average_cost_subquery.c.average_cost, 
            )
            .join(average_cost_subquery, TechnologicalMeanTable.id == average_cost_subquery.c.id)
        )
        return self.session.execute(query).all()

    def maintenance_by_classroom(self):
        """
        Generate comprehensive maintenance statistics by classroom.
        Returns:
            Tuple containing:
            - List of maintenance counts by classroom and mean type
            - List of total maintenance counts by classroom for the last 2 years
        """
        # Consulta para mantenimientos por aula y tipo de medio
        query = select(MeanTable.type, ClassroomTable.number, func.count().label("count"))
        query = query.join(ClassroomTable, ClassroomTable.entity_id == MeanTable.classroom_id)
        query = query.join(MeanMaintenanceTable, MeanTable.entity_id == MeanMaintenanceTable.mean_id)
        query = query.group_by(MeanTable.type, ClassroomTable.number).order_by(ClassroomTable.number, MeanTable.type)

        # Consulta para total de mantenimientos después de dos años
        maintenance_after_two_years = select(ClassroomTable.number, func.count().label("count"))
        maintenance_after_two_years = maintenance_after_two_years.join(MeanTable, 
                                        ClassroomTable.entity_id == MeanTable.classroom_id)
        maintenance_after_two_years = maintenance_after_two_years.join(MeanMaintenanceTable, 
                                        MeanTable.entity_id == MeanMaintenanceTable.mean_id)
        maintenance_after_two_years = maintenance_after_two_years.group_by(ClassroomTable.number)
        maintenance_after_two_years = maintenance_after_two_years.where(
            MeanMaintenanceTable.date >= datetime.now(timezone.utc) - timedelta(days=730))
        maintenance_after_two_years = maintenance_after_two_years.order_by(ClassroomTable.number)
        
        by_classroom = self.session.execute(query).all()
        maintenance_total = self.session.execute(maintenance_after_two_years).all()
    
        return by_classroom, maintenance_total
    
   
