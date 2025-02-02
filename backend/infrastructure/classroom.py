from backend.domain.schemas.classroom import ClassroomCreateModel, ClassroomModel
from backend.domain.models.tables import ClassroomTable, MeanTable
from sqlalchemy.orm import Session
from backend.domain.filters.classroom import ClassroomFilterSchema, ClassroomFilterSet, ClassroomChangeRequest
from sqlalchemy import select, update
import uuid

from .. import IRepository

class ClassroomRepository(IRepository[ClassroomCreateModel,ClassroomModel, ClassroomChangeRequest,ClassroomFilterSchema]):
    def __init__(self, session):   
        super().__init__(session)

    def create(self, entity: ClassroomCreateModel) -> ClassroomTable :
        new_classroom = ClassroomTable(**entity.model_dump())
        self.session.add(new_classroom)
        self.session.commit()
        return new_classroom
    
    def delete(self, entity: ClassroomTable) -> None :
        self.session.delete(entity)
        self.session.commit()

    def update(self, changes : ClassroomChangeRequest , entity : ClassroomModel) -> ClassroomModel:
        query = update(ClassroomTable).where(ClassroomTable.entity_id == entity.id)
        
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        self.session.execute(query)
        self.session.commit()
        return entity
    
    def get_by_id(self, id: str ) -> ClassroomTable :
        query = self.session.query(ClassroomTable)
        query = query.filter(ClassroomTable.entity_id == id)

        return self.session.execute(query).scalars().first()
    
    def get(self, filter_params: ClassroomFilterSchema) -> list[ClassroomTable] :
        query = select(ClassroomTable)
        query = query.outerjoin(MeanTable, ClassroomTable.entity_id == MeanTable.classroom_id)
        filter_set = ClassroomFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        query = query.group_by(ClassroomTable, MeanTable)
        query = query.order_by(ClassroomTable.entity_id)
        return self.session.execute(query).all()
    
    