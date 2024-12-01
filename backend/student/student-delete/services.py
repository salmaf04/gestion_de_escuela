from student.student_common.schemas import StudentModel
from sqlalchemy.orm import Session
from database.tables import StudentTable
import uuid

class TeacherDeletionService:
    def delete_student(self, session: Session, student: StudentModel) -> None :
        session.delete(student)
        session.commit()

class StudentPaginationService :
    def get_student_by_email(self, session: Session, id:uuid.UUID ) -> StudentTable :
        query = session.query(StudentTable).filter(StudentTable.entity_id == id)

        result = query.scalar()

        return result