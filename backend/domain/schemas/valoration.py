"""
Pydantic models for teacher evaluation/valoration data validation and serialization.
These models define the structure for creating and representing teacher evaluations.
"""

from pydantic import BaseModel, field_validator
import uuid 
from backend.domain.schemas.exceptions import ValidationException
from fastapi import HTTPException


class ValorationCreateModel(BaseModel):
    """
    Pydantic model for creating a new teacher evaluation.
    Includes validation for grade value.
    Attributes:
        - teacher_id: UUID of the teacher being evaluated
        - student_id: UUID of the student giving the evaluation
        - subject_id: UUID of the subject being evaluated
        - course_id: UUID of the course context
        - grade: Integer value of the evaluation (0-10)
    """
    teacher_id: uuid.UUID
    student_id: uuid.UUID
    subject_id: uuid.UUID
    course_id: uuid.UUID
    grade: int

    @field_validator("grade")
    def grade_must_be_valid(cls, grade):
        """
        Validates that the grade value is between 0 and 10.
        Raises HTTP 400 error if value is outside valid range.
        """
        try:
            if grade < 0 or grade > 10:
                raise ValidationException("Invalid grade")
        except ValidationException as e:
            raise HTTPException(status_code=400, detail=str(e))
        return grade

class ValorationModel(BaseModel):
    """
    Pydantic model for representing a complete evaluation record.
    Used for responses and data serialization.
    Attributes:
        - id: UUID identifier for the evaluation
        - teacher_id: UUID of the evaluated teacher
        - student_id: UUID of the evaluating student (optional)
        - subject_id: UUID of the evaluated subject
        - course_id: UUID of the course context
        - grade: Integer value of the evaluation
    """
    id: uuid.UUID
    teacher_id: uuid.UUID
    student_id: uuid.UUID | None
    subject_id: uuid.UUID
    course_id: uuid.UUID
    grade: int


class TeacherSubjectValoration(BaseModel):
    """
    Pydantic model for representing a teacher's performance in a specific subject.
    Attributes:
        - subject_id: UUID of the subject
        - average_subject_performance: Float value representing average performance
    """
    subject_id: uuid.UUID
    average_subject_performance: float

class TeacherValoration(BaseModel):
    """
    Pydantic model for representing a teacher's overall evaluation summary.
    Attributes:
        - id: UUID identifier for the teacher
        - performance: List of performance metrics by subject
    """
    id: uuid.UUID
    performance: list[TeacherSubjectValoration]