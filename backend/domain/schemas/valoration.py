from pydantic import BaseModel
import uuid 


class ValorationCreateModel(BaseModel):
    teacher_id: uuid.UUID
    student_id: uuid.UUID
    subject_id: uuid.UUID
    course_id: uuid.UUID
    grade: int

class ValorationModel(ValorationCreateModel):
    id : uuid.UUID