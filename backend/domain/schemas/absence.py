from pydantic import BaseModel
import uuid
from backend.domain.schemas.student import StudentModel

class AbsenceCreateModel(BaseModel):
    student_id: uuid.UUID
    subject_id: uuid.UUID
    date: str

class AbsenceModel(AbsenceCreateModel):
    id : uuid.UUID

