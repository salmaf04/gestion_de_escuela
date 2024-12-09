from sqlalchemy.orm import Session
from backend.domain.schemas.mean_mainteniance import MeanMaintenanceCreateModel, MeanMaintenanceModel
from backend.domain.models.tables import MeanMaintenianceTable
from sqlalchemy import select, update
from backend.application.services.mean import MeanPaginationService
from backend.application.services.my_date import DatePaginationService
from backend.domain.filters.mean_mainteniance import MeanMaintenanceFilterSet , MeanMaintenanceFilterSchema
from backend.domain.models.tables import MeanMaintenianceTable


class MeanMaintenanceCreateService :

    def create_mean_maintenance(self, session: Session, mean_maintenance:MeanMaintenanceCreateModel) -> MeanMaintenianceTable :
        mean_maintenance_dict = mean_maintenance.model_dump()
        new_mean_maintenance = MeanMaintenianceTable(**mean_maintenance_dict)
        
        mean = MeanPaginationService().get_mean_by_id(session=session, id=mean_maintenance.mean_id)
        date = DatePaginationService().get_date_by_id(session=session, id=mean_maintenance.date_id)

        new_mean_maintenance.mean = mean
        new_mean_maintenance.date = date

        mean.mean_mainteniance_association.append(new_mean_maintenance)
        date.mean_mainteniance_association.append(new_mean_maintenance)

        session.add(new_mean_maintenance)
        session.commit()
        return new_mean_maintenance
    
class MeanMaintenancePaginationService :
    def get_mean_maintenance(self, session: Session, filter_params: MeanMaintenanceFilterSchema) -> list[MeanMaintenianceTable] :
        query = select(MeanMaintenianceTable)
        filter_set = MeanMaintenanceFilterSet(session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True)) 
        return session.execute(query).scalars().all()