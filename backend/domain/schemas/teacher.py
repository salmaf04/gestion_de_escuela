from pydantic import BaseModel, Field
import uuid
from typing import Optional
from backend.domain.schemas.user import UserCreateModel
from backend.domain.schemas.subject import SubjectModel

"""
This module defines Pydantic models for managing teacher data.

Classes:
- TeacherModel: A Pydantic model representing a teacher, including attributes such as ID, name, specialty, contract type, experience, email, username, salary, list of subjects, valoration, and alert status.
- TeacherCreateModel: A Pydantic model for creating a new teacher, extending the UserCreateModel with additional attributes specific to teachers.

Dependencies:
- Pydantic's BaseModel for defining data validation and serialization.
- UUID for handling unique identifiers.
- Optional from typing for optional fields.
- UserCreateModel from backend.domain.schemas.user for user-related attributes.

Attributes:
- id (uuid.UUID): The unique identifier for the teacher.
- name (str): The name of the teacher.
- lastname (str): The lastname of the teacher.
- specialty (str): The specialty of the teacher.
- contract_type (str): The contract type of the teacher.
- experience (int): The years of experience the teacher has.
- email (str): The email address of the teacher.
- username (str): The username of the teacher.
- salary (float | None): The salary of the teacher, optional.
- list_of_subjects (list[str]): The list of subjects the teacher is associated with.
- valoration (float | str | None): The valoration of the teacher, optional.
- alert (int | None): The alert status of the teacher, default is 0.
"""
class TeacherModel(BaseModel):
    id : uuid.UUID
    name: str
    lastname: str
    specialty: str
    contract_type: str  
    experience: int
    email: str
    username: str
    salary: float | None = None
    list_of_subjects: list[SubjectModel]
    valoration : Optional[float | str ] = None
    alert : int | None = 0
    
class TeacherCreateModel(UserCreateModel):
    specialty: str
    contract_type: str
    experience: int
    salary: float
    list_of_subjects: list[str]
    