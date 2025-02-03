from backend.domain.schemas.classroom import ClassroomCreateModel, ClassroomModel
from backend.domain.models.tables import ClassroomTable, MeanTable
from sqlalchemy.orm import Session
from backend.domain.filters.classroom import ClassroomFilterSchema, ClassroomFilterSet, ClassroomChangeRequest
from sqlalchemy import select, update
import uuid
from backend.infrastructure.repositories.classroom import ClassroomRepository

class ClassroomCreateService :
    def __init__(self, session):
        self.repo_instance = ClassroomRepository(session)

    def create_classroom(self, classroom: ClassroomCreateModel) -> ClassroomTable :
        return self.repo_instance.create(classroom)
class ClassroomDeletionService:
    def __init__ (self, session):
        self.repo_instance = ClassroomRepository(session)

    def delete_classroom(self, classroom: ClassroomModel) -> None :
        return self.repo_instance.delete(classroom)
        
class ClassroomUpdateService :
    def __init__ (self, session):
        self.repo_instance = ClassroomRepository(session)

    def update_one(self, changes : ClassroomChangeRequest , classroom : ClassroomModel ) -> ClassroomModel: 
        return self.repo_instance.update(changes, classroom)
class ClassroomPaginationService :
    def __init__ (self, session):
        self.repo_instance = ClassroomRepository(session)

    def get_classroom_by_id(self, id:uuid.UUID ) -> ClassroomTable :
        return self.repo_instance.get_by_id(id)
    
    def get_classroom(self, filter_params: ClassroomFilterSchema)  :
        return self.repo_instance.get(filter_params)
