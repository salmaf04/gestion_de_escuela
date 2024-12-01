from teacher.teacher_common.schemas import TeacherModel
from sqlalchemy.orm import Session
from database.tables import TeacherTable
import uuid

class TeacherDeletionService:
    def delete_teacher(self, session: Session, teacher: TeacherModel) -> None :
        session.delete(teacher)
        session.commit()

class TeacherPaginationService :
    def get_teacher_by_email(self, session: Session, id:uuid.UUID ) -> TeacherTable :
        query = session.query(TeacherTable).filter(TeacherTable.entity_id == id)

        result = query.scalar()

        return result
        
