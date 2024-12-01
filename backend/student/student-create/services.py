from sqlalchemy.orm import Session
from .schemas import StudentCreateModel
from database.tables import StudentTable

class StudentCreateService :

    def create_student(self, session: Session, student:StudentCreateModel) -> StudentTable :
        student_dict = student.model_dump()

        new_student = StudentTable(**student_dict)
        session.add(new_student)
        session.commit()
        return new_student

    

class StudentPaginationService :
    def get_student_by_email(self, session: Session, email: str) -> StudentTable :
        query = session.query(StudentTable).filter(StudentTable.email == email)

        result = query.first()

        return result



