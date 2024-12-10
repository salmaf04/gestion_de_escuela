from pydantic import BaseModel
import uuid 


class NoteCreateModel(BaseModel):
    teacher_id: uuid.UUID
    student_id: uuid.UUID
    subject_id: uuid.UUID
    note_value: int

class NoteModel(NoteCreateModel):
    id : uuid.UUID