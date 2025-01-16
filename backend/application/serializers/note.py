from backend.domain.schemas.note import NoteModel
from backend.domain.models.tables import StudentNoteTable
from pydantic import BaseModel
import uuid
from backend.application.services.student import StudentPaginationService
from fastapi.encoders import jsonable_encoder

class NoteLessThanFifty(BaseModel) :
    name : str
    student_id : uuid.UUID
    teacher_name : str
    teacher_valoration : float | None
   

class NoteMapper :
    def to_api(self, note: StudentNoteTable) -> NoteModel :
        return NoteModel(
            id = note.entity_id,
            teacher = note.teacher.name,
            student = note.student.name,
            subject = note.subject.name,
            note_value = note.note_value
        )
    
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
        


