from pydantic import BaseModel
import uuid

class AbsenceCreateModel(BaseModel):
    student_id: uuid.UUID
    course_id: uuid.UUID
    subject_id: uuid.UUID
    absences: int

class AbsenceModel(AbsenceCreateModel):
    id : uuid.UUID
    