from pydantic import BaseModel, field_validator
import uuid 
from backend.domain.schemas.exceptions import ValidationException
from fastapi import HTTPException



class NoteCreateModel(BaseModel):
    teacher_id: uuid.UUID
    student_id: uuid.UUID
    subject_id: uuid.UUID
    note_value: int

    @field_validator("note_value")
    def note_value_must_be_valid(cls, note_value):
        try :
            if note_value < 0 or note_value > 100:
                raise ValidationException("Invalid note value")
        except ValidationException as e:
            raise HTTPException(status_code=400, detail=str(e))
        return note_value
    
    
class NoteModel(BaseModel):
    teacher : str
    student : str
    subject : str
    id : uuid.UUID
    note_value : int
    last_modified_by : uuid.UUID