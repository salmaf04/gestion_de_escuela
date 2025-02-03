from sqlalchemy.orm import Session
from sqlalchemy import select, and_, delete
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.classroom import ClassroomPaginationService
from .base import IRepository
from backend.domain.models.tables import TeacherTable, ClassroomTable, teacher_request_classroom_table

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

    def get_by_id(self, teacher_id: str, classroom_id : str ) -> None :
        query = select(teacher_request_classroom_table)
        query = query.where(
            and_(
                teacher_request_classroom_table.c.teacher_id == teacher_id,
                teacher_request_classroom_table.c.classroom_id == classroom_id
            )
        )
        return self.session.execute(query).first()
        

    def delete(self, entity: None, classroom_request) -> None :
        stmt = delete(teacher_request_classroom_table).where(
            and_(
                teacher_request_classroom_table.c.teacher_id == classroom_request.teacher_id,
                teacher_request_classroom_table.c.classroom_id == classroom_request.classroom_id,
            )
        )
        self.session.execute(stmt)
        self.session.commit()
