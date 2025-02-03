from sqlalchemy.orm import Session
from sqlalchemy import select, update, func
from backend.domain.filters.student import StudentFilterSet , StudentFilterSchema, StudentChangeRequest
from backend.domain.schemas.student import StudentCreateModel, StudentModel
from backend.domain.models.tables import StudentTable, StudentNoteTable, TeacherTable, CourseTable, SubjectTable, teacher_subject_table
from backend.application.services.course import CoursePaginationService
from ..utils.auth import get_password_hash, get_password
from ..utils.note_average import  calculate_student_average
import uuid
from backend.infrastructure.repositories.student import StudentRepository


class StudentCreateService :
    def __init__(self, session):
        self.repo_instance = StudentRepository(session)

    def create_student(self, student:StudentCreateModel) -> StudentTable :
        return self.repo_instance.create(student)
   
class StudentDeletionService:
    def __init__(self, session):
        self.repo_instance = StudentRepository(session)

    def delete_student(self, student: StudentModel) -> None :
        return self.repo_instance.delete(student)
            
class StudentUpdateService :
    def __init__(self, session):
        self.repo_instance = StudentRepository(session)

    def update_one(self, changes : StudentChangeRequest , student : StudentModel ) -> StudentModel: 
        return self.repo_instance.update(changes, student)
        
class StudentPaginationService :
    def __init__(self, session):
        self.repo_instance = StudentRepository(session)

    def get_student_by_email(self, email: str) -> StudentTable :
        self.repo_instance.get_student_by_email(email)
       
    def get_student_by_id(self, id:uuid.UUID ) -> StudentTable :
        return self.repo_instance.get_by_id(id)
        
    def get_students(self, filter_params: StudentFilterSchema) -> list[StudentTable] :
        return self.repo_instance.get(filter_params)
    
    def get_academic_information(self, student_id: str) :
        return self.repo_instance.get_academic_information(student_id)
        
    def get_students_by_teacher(self, teacher_id: str) :
        return self.repo_instance.get_students_by_teacher(teacher_id)
    
class UpdateNoteAverageService : 
    def update_note_average(self, session: Session, student_id: str, new_note : int ) : 
        new_avergage = calculate_student_average(session=session, student_id=student_id, new_note=new_note)
        query = update(StudentTable).where(StudentTable.id == student_id).values(average_note=new_avergage)
        session.execute(query)
        session.commit()