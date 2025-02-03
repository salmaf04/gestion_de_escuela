from pydantic import BaseModel
import uuid
from backend.domain.schemas.user import UserCreateModel

"""
This module defines Pydantic models for representing student data and performance in the application.

Classes:
    StudentModel: A model representing a student with detailed attributes.
    StudentCreateModel: A model for creating new student records, extending user creation attributes.
    StudentSubjectPerformance: A model representing a student's performance in a specific subject.
    StudentAcademicPerformance: A model representing a student's overall academic performance.

Class Details:

1. StudentModel:
    - Inherits from Pydantic's BaseModel.
    - Represents a student with detailed attributes.
    - Attributes:
        - id: The unique identifier of the student (UUID).
        - name: The first name of the student (string).
        - lastname: The last name of the student (string).
        - age: The age of the student (integer).
        - email: The email address of the student (string).
        - extra_activities: A boolean indicating if the student participates in extra activities.
        - username: The username of the student (string).
        - hash_password: The hashed password of the student (string).
        - course_id: The unique identifier of the course the student is enrolled in (UUID).

2. StudentCreateModel:
    - Inherits from UserCreateModel.
    - Represents the data required to create a new student, including user creation attributes.
    - Attributes:
        - age: The age of the student (integer).
        - extra_activities: A boolean indicating if the student participates in extra activities.
        - course_id: The unique identifier of the course the student is enrolled in (UUID).

3. StudentSubjectPerformance:
    - Inherits from Pydantic's BaseModel.
    - Represents a student's performance in a specific subject.
    - Attributes:
        - subject_id: The unique identifier of the subject (UUID).
        - average_subject_performance: The average performance of the student in the subject (float).

4. StudentAcademicPerformance:
    - Inherits from Pydantic's BaseModel.
    - Represents a student's overall academic performance.
    - Attributes:
        - id: The unique identifier of the student (UUID).
        - performance: A list of StudentSubjectPerformance objects representing the student's performance in various subjects.

Dependencies:
    - Pydantic for data validation and serialization.
    - UUID for handling unique identifiers.
    - UserCreateModel for user-related attributes during student creation.
"""
class StudentModel(BaseModel):
    id : uuid.UUID
    name: str
    lastname: str
    age: int
    email: str
    extra_activities: bool
    username: str
    hash_password: str
    course_id : uuid.UUID
    
class StudentCreateModel(UserCreateModel):
    age: int
    extra_activities: bool
    course_id : uuid.UUID

class StudentSubjectPerformance(BaseModel):
    subject_id : uuid.UUID
    average_subject_performance : float

class StudentAcademicPerformance(BaseModel):
    id : uuid.UUID
    performance : list[StudentSubjectPerformance]
    



