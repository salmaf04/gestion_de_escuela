from sqlalchemy.orm import Session
from .schemas import TeacherCreateModel, TeacherModel
from database.tables import TeacherTable

class TeacherCreateService :

    def create_teacher(self, session: Session, teacher: TeacherCreateModel) -> TeacherTable :
        teacher_dict = teacher.model_dump()

        new_teacher = TeacherTable(**teacher_dict)
        session.add(new_teacher)
        session.commit()
        return new_teacher
    

class TeacherPaginationService :
    def get_teacher_by_email(self, session: Session, email: str) -> TeacherTable :
        query = session.query(TeacherTable).filter(TeacherTable.email == email)

        result = query.first()

        return result

