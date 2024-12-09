from backend.domain.schemas.classroom import ClassroomCreateModel, ClassroomModel
from backend.domain.models.tables import ClassroomTable
from sqlalchemy.orm import Session
from backend.domain.filters.classroom import ClassroomFilterSchema, ClassroomFilterSet, ChangeRequest
from sqlalchemy import select, update
import uuid

class ClassroomCreateService :
    def create_classroom(self, session: Session, classroom: ClassroomCreateModel) -> ClassroomTable :
        new_classroom = ClassroomTable(**classroom.dict())
        session.add(new_classroom)
        session.commit()
        return new_classroom
    
class ClassroomDeletionService:
    def delete_classroom(self, session: Session, classroom: ClassroomTable) -> None :
        session.delete(classroom)
        session.commit()
        
        
class ClassroomUpdateService :
    def update_one(self, session : Session , changes : ChangeRequest , classroom : ClassroomModel ) -> ClassroomModel: 
        query = update(ClassroomTable).where(ClassroomTable.entity_id == classroom.id)
        
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        session.execute(query)
        session.commit()
        
        classroom = classroom.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return classroom
           

class ClassroomPaginationService :
    
    def get_classroom_by_id(self, session: Session, id:uuid.UUID ) -> ClassroomTable :
        query = session.query(ClassroomTable).filter(ClassroomTable.entity_id == id)

        result = query.scalar()

        return result
    
    def get_classroom(self, session: Session, filter_params: ClassroomFilterSchema) -> list[ClassroomTable] :
        query = select(ClassroomTable)
        filter_set = ClassroomFilterSet(session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return session.execute(query).scalars().all()