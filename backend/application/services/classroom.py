from backend.domain.schemas.classroom import ClassroomCreateModel
from backend.domain.models.tables import ClassroomTable
from sqlalchemy.orm import Session


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
        