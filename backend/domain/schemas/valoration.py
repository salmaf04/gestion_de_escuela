from pydantic import BaseModel, field_validator
import uuid 
from backend.domain.schemas.exceptions import ValidationException
from fastapi import HTTPException


class ValorationCreateModel(BaseModel):
    teacher_id: uuid.UUID
    student_id: uuid.UUID
    subject_id: uuid.UUID
    course_id: uuid.UUID
    grade: int

    @field_validator("grade")
    def grade_must_be_valid(cls, grade):
        try :
            if grade < 0 or grade > 10:
                raise ValidationException("Invalid grade")
        except ValueError as e:
            return HTTPException(status_code=400, detail=str(e))
        return grade

class ValorationModel(ValorationCreateModel):
    id : uuid.UUID


class TeacherSubjectValoration(BaseModel):
    subject_id : uuid.UUID
    average_subject_performance : float

class TeacherValoration(BaseModel):
    id : uuid.UUID
    performance : list[TeacherSubjectValoration]