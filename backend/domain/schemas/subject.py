from pydantic import BaseModel
import uuid
from backend.domain.schemas.classroom import ClassroomModelPost
from backend.domain.schemas.course import CourseModel

"""
This module defines Pydantic models for representing subject data in the application.

Classes:
    SubjectModel: A model representing a subject with detailed attributes.
    SubjectCreateModel: A model for creating new subject records.

Class Details:

1. SubjectModel:
    - Inherits from Pydantic's BaseModel.
    - Represents a subject with detailed attributes.
    - Attributes:
        - id: The unique identifier of the subject (UUID).
        - name: The name of the subject (string).
        - hourly_load: The number of hours allocated to the subject (integer).
        - study_program: The identifier of the study program the subject belongs to (integer).
        - classroom_id: The unique identifier of the classroom associated with the subject (UUID or None).
        - course_id: The unique identifier of the course the subject is part of (UUID).

2. SubjectCreateModel:
    - Inherits from Pydantic's BaseModel.
    - Represents the data required to create a new subject.
    - Attributes:
        - name: The name of the subject (string).
        - hourly_load: The number of hours allocated to the subject (integer).
        - study_program: The identifier of the study program the subject belongs to (integer).
        - classroom_id: The unique identifier of the classroom associated with the subject (UUID).
        - course_id: The unique identifier of the course the subject is part of (UUID).

Dependencies:
    - Pydantic for data validation and serialization.
    - UUID for handling unique identifiers.
"""
class SubjectModel(BaseModel):
    id : uuid.UUID
    name: str
    hourly_load: int
    study_program: int
    classroom : ClassroomModelPost | None
    course : CourseModel | None
    
class SubjectCreateModel(BaseModel):
    name: str
    hourly_load: int
    study_program: int
    classroom_id : uuid.UUID 
    course_id : uuid.UUID