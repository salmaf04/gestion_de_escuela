from sqlalchemy.orm import Session
from sqlalchemy import update
from .filters import ChangeRequest
import uuid 
from database.tables import TeacherTable
from teacher.teacher_common.schemas import  TeacherModel

class TeacherUpdateService :
    def update_one(self, session : Session , changes : ChangeRequest , teacher : TeacherModel ) -> TeacherModel: 
        query = update(TeacherTable).where(TeacherTable.entity_id == teacher.id)
        
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        session.execute(query)
        session.commit()
        
        teacher = teacher.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return teacher

class TeacherListingService :
    def get_teacher_by_id(self, session: Session, id : int) -> TeacherTable :
        query = session.query(TeacherTable).filter(TeacherTable.entity_id == id)

        result = query.first()

        return result
    
