from sqlalchemy.orm import Session
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.classroom import ClassroomPaginationService
from .base import IRepository
from backend.domain.models.tables import TeacherTable, ClassroomTable

class ClassroomRequestRepository(IRepository[None,None, None,None]):
    def __init__(self, session):
        super().__init__(session)

    def create(self, teacher : TeacherTable, classroom : ClassroomTable) :
        teacher.classroom_request.append(classroom)
        self.session.commit()
        return classroom.entity_id
    
    def get(self, filter_params: None) -> list[None] :
        pass

    def update(self, changes : None , entity : None) -> None:
        pass

    def get_by_id(self, id: str ) -> None :
        pass

    def delete(self, entity: None) -> None :
        pass

