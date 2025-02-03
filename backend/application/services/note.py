from sqlalchemy.orm import Session
from backend.domain.schemas.note import NoteCreateModel, NoteModel
from backend.domain.models.tables import StudentNoteTable, StudentTable, TeacherTable
from backend.application.services.student import StudentPaginationService
from backend.application.services.subject import SubjectPaginationService
from backend.application.services.teacher import TeacherPaginationService
from backend.domain.filters.note import NoteFilterSet , NoteFilterSchema, NoteChangeRequest
from sqlalchemy import select, func, update
from backend.application.services.student import UpdateNoteAverageService
from backend.infrastructure.repositories.note import NoteRepository

class NoteCreateService :
    def __init__(self, session):
        self.repo_instance = NoteRepository(session)
        self.student_pagination_service = StudentPaginationService(session)
        self.subject_pagination_service = SubjectPaginationService(session)
        self.teacher_pagination_service = TeacherPaginationService(session)

    def create_note(self, note: NoteCreateModel, modified_by : str) -> StudentNoteTable :
        student = self.student_pagination_service.get_student_by_id(id=note.student_id)
        subject = self.subject_pagination_service.get_subject_by_id(id=note.subject_id)
        teacher = self.teacher_pagination_service.get_teacher_by_id(id=note.teacher_id)
        return self.repo_instance.create(note, modified_by, student, subject, teacher)
        

class NotePaginationService :
    def __init__(self, session):
        self.repo_instance = NoteRepository(session)

    def get_note_by_id(self,id : str) -> StudentNoteTable :
        return self.repo_instance.get_by_id(id)
    
    def get_note(self, filter_params: NoteFilterSchema) -> list[StudentNoteTable] :
        return self.repo_instance.get(filter_params)
    
    def grade_less_than_fifty(self) :
        return self.repo_instance.grade_less_than_fifty()
    
    def get_note_by_student(self, student_id: str) -> list[StudentNoteTable] :
        return self.repo_instance.get_note_by_student(student_id=student_id)
        
class NoteUpdateService() :
    def __init__(self, session):
        self.repo_instance = NoteRepository(session)

    def update_note(self, note : NoteModel, modified_by : str, new_note : NoteChangeRequest ) :
        return self.repo_instance.update(new_note, note, modified_by=modified_by)

    




       