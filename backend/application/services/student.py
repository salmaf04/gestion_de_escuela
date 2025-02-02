from sqlalchemy.orm import Session
from sqlalchemy import select, update, func
from backend.domain.filters.student import StudentFilterSet , StudentFilterSchema, StudentChangeRequest
from backend.domain.schemas.student import StudentCreateModel, StudentModel
from backend.domain.models.tables import StudentTable, StudentNoteTable, TeacherTable, CourseTable, SubjectTable, teacher_subject_table
from backend.application.services.course import CoursePaginationService
from ..utils.auth import get_password_hash, get_password
from ..utils.note_average import  calculate_student_average
import uuid



class StudentCreateService :

    def create_student(self, session: Session, student:StudentCreateModel) -> StudentTable :
        student_dict = student.model_dump(exclude={'password'})
        hashed_password = get_password_hash(get_password(student))
        new_student = StudentTable(**student_dict, hashed_password=hashed_password)
        session.add(new_student)
        session.commit()
        return new_student


class StudentDeletionService:
    def delete_student(self, session: Session, student: StudentModel) -> None :
        session.delete(student)        
        session.commit()
            

class StudentUpdateService :
    def update_one(self, session : Session , changes : StudentChangeRequest , student : StudentModel ) -> StudentModel: 
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
    
    
    def get_academic_information(self, session: Session , student_id: str) :
        query = select(StudentTable.id , StudentNoteTable.subject_id , (func.sum(StudentNoteTable.note_value)/func.count()).label("academic_performance"))
        query = query.join(StudentNoteTable, StudentTable.id == StudentNoteTable.student_id)
        query = query.where(StudentTable.id == student_id)
        query = query.group_by(StudentTable.id , StudentNoteTable.subject_id)
        print(session.execute(query).all())
        result = session.execute(query).all()
        return result
    
    def get_students_by_teacher(self, session: Session, teacher_id: str) :
        query = select(TeacherTable.id, SubjectTable, CourseTable, StudentTable)
        query = query.join(teacher_subject_table, TeacherTable.id == teacher_subject_table.c.teacher_id)
        query = query.join(SubjectTable, teacher_subject_table.c.subject_id == SubjectTable.entity_id)
        query = query.join(CourseTable, SubjectTable.course_id == CourseTable.entity_id)
        query = query.join(StudentTable, CourseTable.entity_id == StudentTable.course_id)
        query = query.where(TeacherTable.id == teacher_id)
        query = query.distinct(StudentTable.id)
        return session.execute(query).all()

    
        

class UpdateNoteAverageService : 
    def update_note_average(self, session: Session, student_id: str, new_note : int ) : 
        new_avergage = calculate_student_average(session=session, student_id=student_id, new_note=new_note)
        query = update(StudentTable).where(StudentTable.id == student_id).values(average_note=new_avergage)
        session.execute(query)
        session.commit()