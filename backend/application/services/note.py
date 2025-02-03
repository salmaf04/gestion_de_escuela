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

"""
This module defines services for creating, retrieving, and updating student note records.

Classes:
    NoteCreateService: A service for creating new student note records.
    NotePaginationService: A service for retrieving student note records based on various criteria.
    NoteUpdateService: A service for updating student note records.

Classes Details:

1. NoteCreateService:
    - This service is responsible for creating new student note records.
    - It utilizes the NoteRepository to interact with the database.
    - It also uses StudentPaginationService, SubjectPaginationService, and TeacherPaginationService to retrieve student, subject, and teacher details.
    
    Methods:
        - __init__(session): Initializes the service with a database session and sets up necessary service instances.
        - create_note(note: NoteCreateModel, modified_by: str) -> StudentNoteTable: 
            Creates a new student note record using the provided NoteCreateModel and returns the created StudentNoteTable object.

2. NotePaginationService:
    - This service is responsible for retrieving student note records based on different criteria.
    - It uses the NoteRepository to fetch data from the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - get_note_by_id(id: str) -> StudentNoteTable: 
            Retrieves a student note record by the specified ID.
        - get_note(filter_params: NoteFilterSchema) -> list[StudentNoteTable]: 
            Retrieves a list of student notes based on the provided filter parameters.
        - grade_less_than_fifty(): 
            Retrieves student notes with grades less than fifty.
        - get_note_by_student(student_id: str) -> list[StudentNoteTable]: 
            Retrieves student notes for a specific student identified by the student_id.

3. NoteUpdateService:
    - This service is responsible for updating student note records.
    - It uses the NoteRepository to perform update operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - update_note(note: NoteModel, modified_by: str, new_note: NoteChangeRequest): 
            Updates the specified student note record with the provided changes.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - NoteRepository for database operations related to student notes.
    - NoteCreateModel, NoteModel, StudentNoteTable, and other domain models for data representation.
    - NoteFilterSchema and NoteFilterSet for filtering student note records.
    - StudentPaginationService, SubjectPaginationService, and TeacherPaginationService for retrieving related information.
"""

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
        
    def get_note_by_student_by_teacher(self, teacher_id: str) -> list[StudentNoteTable] :        
        return self.repo_instance.get_note_by_student_by_teacher(teacher_id=teacher_id)
class NoteUpdateService() :
    def __init__(self, session):
        self.repo_instance = NoteRepository(session)

    def update_note(self, note : NoteModel, modified_by : str, new_note : NoteChangeRequest ) :
        return self.repo_instance.update(new_note, note, modified_by=modified_by)

    




       