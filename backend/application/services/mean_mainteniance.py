from sqlalchemy.orm import Session
from backend.domain.schemas.mean_mainteniance import MeanMaintenanceCreateModel, MeanMaintenanceModel
from backend.domain.models.tables import MeanMaintenianceTable
from sqlalchemy import select, update
from backend.application.services.mean import MeanPaginationService
from backend.application.services.my_date import DatePaginationService
from backend.domain.filters.mean_mainteniance import MeanMaintenanceFilterSet , MeanMaintenanceFilterSchema
from backend.domain.models.tables import MeanMaintenianceTable, TechnologicalMeanTable, MeanTable, ClassroomTable
import uuid
from datetime import datetime, timedelta, timezone
from sqlalchemy import func
from sqlalchemy import extract, and_



class MeanMaintenanceCreateService :

    def create_mean_maintenance(self, session: Session, mean_maintenance:MeanMaintenanceCreateModel) -> MeanMaintenianceTable :
        check_replacement_service = CheckReplacementService()
        
        
        mean_maintenance_dict = mean_maintenance.model_dump()
        new_mean_maintenance = MeanMaintenianceTable(**mean_maintenance_dict)
        
        mean = MeanPaginationService().get_mean_by_id(session=session, id=mean_maintenance.mean_id)
        date = DatePaginationService().get_date_by_id(session=session, id=mean_maintenance.date_id)
        
        check_replacement = check_replacement_service.check_replacement(session=session, date=date.date, mean_id=mean_maintenance.mean_id)

        if check_replacement :
            mean.to_be_replaced = True

        new_mean_maintenance.mean = mean
        new_mean_maintenance.date = date.date

        mean.mean_mainteniance_association.append(new_mean_maintenance)

        session.add(new_mean_maintenance)
        session.commit()
        return new_mean_maintenance
    
class MeanMaintenancePaginationService :
    def get_mean_maintenance(self, session: Session, filter_params: MeanMaintenanceFilterSchema) -> list[MeanMaintenianceTable] :
        query = select(MeanMaintenianceTable)
        filter_set = MeanMaintenanceFilterSet(session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True)) 
        return session.execute(query).scalars().all()
    

    def get_mainenance_by_classroom(self, session: Session) :
        query = select(MeanMaintenianceTable.mean.classroom, MeanMaintenianceTable.mean.type, func.count(MeanMaintenianceTable.entity_id).label("count"))
        query.where(MeanMaintenianceTable.date == datetime.now(timezone.utc) - timedelta(days=730))
        query.group_by(MeanMaintenanceModel.mean.classroom, MeanMaintenanceModel.mean.type)

        return session.execute(query).scalars().all()


    def maintenace_average(self, session: Session) :
        current_year = datetime.now(timezone.utc).year

        average_cost_subquery = (
        select(
            TechnologicalMeanTable.id,
            (func.sum(MeanMaintenianceTable.cost) / func.count(MeanMaintenianceTable.entity_id)).label('average_cost'),
            func.count(MeanMaintenianceTable.mean_id).label('maintenance_count')
        )
        .join(MeanMaintenianceTable, TechnologicalMeanTable.id == MeanMaintenianceTable.mean_id)
        .where(MeanMaintenianceTable.date >= datetime.now(timezone.utc) - timedelta(days=365))
        .group_by(TechnologicalMeanTable.id)
        .having(func.count(MeanMaintenianceTable.mean_id) > 2)  # Filtrar medios con más de dos mantenimientos
        .subquery()
    )
    
    # Consulta principal para obtener los detalles de los medios tecnológicos
        query = (
            select(
                TechnologicalMeanTable.id,
                TechnologicalMeanTable.name,
                average_cost_subquery.c.average_cost, 
            )
            .join(average_cost_subquery, TechnologicalMeanTable.id == average_cost_subquery.c.id)
        )

        return session.execute(query).all()
    

    def maintenance_by_classroom(self, session: Session) :

        #Mantenimientos por aula y por tipo de medio
        query = select(MeanTable.type, ClassroomTable.entity_id, func.count().label("count"))
        query = query.join(ClassroomTable, ClassroomTable.entity_id == MeanTable.classroom_id)
        query = query.join(MeanMaintenianceTable, MeanTable.entity_id == MeanMaintenianceTable.mean_id)
        query = query.group_by(MeanTable.type, ClassroomTable.entity_id).order_by(ClassroomTable.entity_id, MeanTable.type)

        # Total de mantenimientos despues de dos años
        mainteniance_after_two_years = select(func.count(MeanMaintenianceTable.entity_id).label("total"))
        mainteniance_after_two_years = mainteniance_after_two_years.where(MeanMaintenianceTable.date >= datetime.now(timezone.utc) - timedelta(days=730))
        
        by_classroom = session.execute(query).all()
        mainteniance_total = session.execute(mainteniance_after_two_years).scalar()
    
        return by_classroom, mainteniance_total
    


class CheckReplacementService :
    def check_replacement(self, session: Session, date : datetime, mean_id : uuid.UUID ) -> bool :
        date = datetime.now(timezone.utc) - timedelta(days=365)
        query = select(func.count(MeanMaintenianceTable.entity_id).label("count"))
        query = query.where(and_(MeanMaintenianceTable.date >= date, MeanMaintenianceTable.mean_id == mean_id))

        result = session.execute(query).scalars().first()

        print(result)

        if result >= 2 : 
            return True
        
        return False

    