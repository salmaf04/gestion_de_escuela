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

class MeanRepository(IRepository[MeanCreateModel,MeanModel, MeanChangeRequest,MeanFilterSchema]):
    def __init__(self, session):
        super().__init__(session)

    def create(self, entity: MeanCreateModel) -> MeanTable :
        table_to_insert = {
            "technological_mean": TechnologicalMeanTable,
            "teaching_material": TeachingMaterialTable,
            "other": OthersTable,
        }
        
        classroom_pagination_service = ClassroomPaginationService()
        classroom = classroom_pagination_service.get_classroom_by_id(session=self.session, id=entity.classroom_id)

        mean_dict = entity.model_dump()
        mean_type = table_to_insert.get(entity.type, None)
    
        if mean_type is None :
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

    def delete(self, entity: MeanModel) -> None :
        self.session.delete(entity)
        self.session.commit()
        
    
    def update(self, changes : MeanChangeRequest , entity : MeanModel ) -> MeanModel:
        query = update(MeanTable).where(MeanTable.entity_id == entity.id)
        
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        self.session.execute(query)
        self.session.commit()
        
        mean = entity.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return mean
        
    def get_by_id(self, id: str ) -> MeanTable :
        query = self.session.query(MeanTable).filter(MeanTable.entity_id == id)

        result = query.scalar()

        return result
    
    def get(self, filter_params: MeanFilterSchema) -> list[MeanTable] :
        query = select(MeanTable)
        filter_set = MeanFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return self.session.execute(query).scalars().all()
    
    def get_avaliable_means(self) -> list[MeanTable] :
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
    

  
