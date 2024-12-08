from sqlalchemy.orm import Session
from sqlalchemy import select, update
from backend.domain.filters.student import StudentFilterSet , StudentFilterSchema, ChangeRequest
from backend.domain.schemas.student import StudentCreateModel, StudentModel
from database.tables import StudentTable
import uuid


class StudentCreateService :

    def create_student(self, session: Session, student:StudentCreateModel) -> StudentTable :
        student_dict = student.model_dump()

        new_student = StudentTable(**student_dict)
        session.add(new_student)
        session.commit()
        return new_student


class StudentDeletionService:
    def delete_student(self, session: Session, student: StudentModel) -> None :
        session.delete(student)
        session.commit()
        

class StudentUpdateService :
    def update_one(self, session : Session , changes : ChangeRequest , student : StudentModel ) -> StudentModel: 
        query = update(StudentTable).where(StudentTable.entity_id == student.id)
        
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        session.execute(query)
        session.commit()
        
        student = student.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return student
           

class StudentPaginationService :
    def get_student_by_email(self, session: Session, email: str) -> StudentTable :
        query = session.query(StudentTable).filter(StudentTable.email == email)

        result = query.first()

        return result
    
    def get_student_by_id(self, session: Session, id:uuid.UUID ) -> StudentTable :
        query = session.query(StudentTable).filter(StudentTable.entity_id == id)

        result = query.scalar()

        return result
    
    def get_students(self, session: Session, filter_params: StudentFilterSchema) -> list[StudentTable] :
        query = select(StudentTable)
        filter_set = StudentFilterSet(session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return session.execute(query).scalars().all()
    




    



