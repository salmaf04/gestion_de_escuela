from pydantic import BaseModel
import uuid
from backend.domain.schemas.student import StudentModel

class AbsenceCreateModel(BaseModel):
    """
    Pydantic model for creating a new absence record.
    Attributes:
        - student_id: UUID of the student who was absent
        - subject_id: UUID of the subject missed
        - date: Date of the absence as string
    """
    student_id: uuid.UUID
    subject_id: uuid.UUID
    date: str

class AbsenceModel(AbsenceCreateModel):
    """
    Pydantic model for representing a complete absence record.
    Inherits all fields from AbsenceCreateModel and adds:
        - id: UUID identifier for the absence record
    """
    id: uuid.UUID

