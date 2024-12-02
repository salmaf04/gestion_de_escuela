from sqlalchemy.orm import Session
from sqlalchemy import update
from .filters import ChangeRequest
from database.tables import StudentTable
from student.student_common.schemas import  StudentModel

class StudentUpdateService :
    def update_one(self, session : Session , changes : ChangeRequest , student : StudentModel ) -> StudentModel: 
        query = update(StudentTable).where(StudentTable.entity_id == student.id)
        
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        session.execute(query)
        session.commit()
        
        student = student.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return student

class StudentListingService :
    def get_student_by_id(self, session: Session, id : int) -> StudentTable :
        query = session.query(StudentTable).filter(StudentTable.entity_id == id)

        result = query.first()

        return result