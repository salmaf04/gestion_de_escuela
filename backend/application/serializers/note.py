from backend.domain.schemas.note import NoteModel
from backend.domain.schemas.student import StudentModel
from backend.domain.schemas.teacher import TeacherModel
from backend.domain.schemas.subject import SubjectModel
from backend.application.serializers.student import StudentMapper
from backend.application.serializers.teacher import TeacherMapper
from backend.application.serializers.subject import SubjectMapper
from backend.domain.models.tables import StudentNoteTable
from pydantic import BaseModel
import uuid
from backend.application.services.student import StudentPaginationService
from fastapi.encoders import jsonable_encoder

"""
This module defines a mapper for converting note data into API representations.

Classes:
    NoteLessThanFifty: A Pydantic model representing notes with values less than fifty.
    NoteMapper: A utility class for mapping StudentNoteTable objects to NoteModel objects and handling notes with values less than fifty.

Class Details:

1. NoteLessThanFifty:
    - Represents notes with values less than fifty.
    - Attributes:
        - name: The name of the student.
        - student_id: The unique identifier of the student.
        - teacher_name: The name of the teacher.
        - teacher_valoration: The valoration of the teacher, if available.

2. NoteMapper:
    - This class provides methods to convert StudentNoteTable objects into NoteModel objects and to handle notes with values less than fifty.
    
    Methods:
        - to_api(note: StudentNoteTable) -> NoteModel: 
            Converts the given StudentNoteTable object into a NoteModel object, mapping the relevant fields such as ID, teacher, student, subject, note value, and last modified by.
        - to_less_than_fifty(data): 
            Converts raw data into a list of NoteLessThanFifty objects, representing notes with values less than fifty.

Dependencies:
    - Pydantic for data validation and serialization.
    - NoteModel for API data representation.
    - StudentNoteTable for database representation.
    - UUID for handling unique identifiers.
    - FastAPI for JSON encoding.
"""
class NoteLessThanFifty(BaseModel) :
    name : str
    student_id : uuid.UUID
    teacher_name : str
    teacher_valoration : float | None

class NoteByTeacher(BaseModel) :
    student : StudentModel
    teacher: TeacherModel
    subject: SubjectModel
    note_value: float
    last_modified_by: uuid.UUID
   
class NoteMapper :
    def to_api(self, data) -> NoteModel :
        subject_mapper = SubjectMapper()
        teacher_mapper = TeacherMapper()
        student_mapper = StudentMapper()
        serialized_values = []
       
        for item in data :
            new_item = NoteByTeacher(
                student = student_mapper.to_api(item[1]),
                teacher = teacher_mapper.to_api_note(item[2]),
                subject = subject_mapper.to_api(item[3]),
                note_value = item[0].note_value,
                last_modified_by = item[0].last_modified_by
            )
            serialized_values.append(new_item)
       
        return serialized_values

    def to_less_than_fifty(self, data) :
        serialized_values = []

        for item in data :
            new_item = NoteLessThanFifty(
                name = item[0],
                student_id = item[1],
                teacher_name= item[2],
                teacher_valoration= item[3]
            )
            serialized_values.append(new_item)

        return serialized_values
        
    def to_note_by_teacher(self, data) :
        subject_mapper = SubjectMapper()
        teacher_mapper = TeacherMapper()
        student_mapper = StudentMapper()
        serialized_values = []
        
        for item in data :
            new_item = NoteByTeacher(
                student = student_mapper.to_api(item[1]),
                teacher = teacher_mapper.to_api_note(item[2]),
                subject = subject_mapper.to_api(item[3]),
                note_value = item[0].note_value,
                last_modified_by = item[0].last_modified_by
            )
            serialized_values.append(new_item)

        return serialized_values
    
    def to_post(self, note: StudentNoteTable) : 
        return NoteModel(
            teacher=note.teacher.name,
            student=note.student.name,
            subject=note.subject.name,
            id = note.entity_id,
            note_value=note.note_value,
            last_modified_by=note.last_modified_by
        )


