"""
Pydantic models for grade/note data validation and serialization.
These models define the structure for creating and representing grades in the system.
"""

from pydantic import BaseModel, field_validator
import uuid 
from backend.domain.schemas.exceptions import ValidationException
from fastapi import HTTPException



class NoteCreateModel(BaseModel):
    """
    Pydantic model for creating a new grade entry.
    Includes validation for note value.
    Attributes:
        - teacher_id: UUID of the teacher assigning the grade
        - student_id: UUID of the student receiving the grade
        - subject_id: UUID of the subject being graded
        - note_value: Integer value of the grade (0-100)
    """
    teacher_id: uuid.UUID
    student_id: uuid.UUID
    subject_id: uuid.UUID
    note_value: int

    @field_validator("note_value")
    def note_value_must_be_valid(cls, note_value):
        """
        Validates that the grade value is between 0 and 100.
        Raises HTTP 400 error if value is outside valid range.
        """
        try:
            if note_value < 0 or note_value > 100:
                raise ValidationException("Invalid note value")
        except ValidationException as e:
            raise HTTPException(status_code=400, detail=str(e))
        return note_value
    
    
class NoteModel(BaseModel):
    """
    Pydantic model for representing a complete grade record.
    Used for responses and data serialization.
    Attributes:
        - teacher: String identifier/name of the teacher
        - student: String identifier/name of the student
        - subject: String identifier/name of the subject
        - id: UUID identifier for the grade record
        - note_value: Integer value of the grade
        - last_modified_by: UUID of user who last modified the grade
    """
    teacher: str
    student: str
    subject: str
    id: uuid.UUID
    note_value: int
    last_modified_by: uuid.UUID