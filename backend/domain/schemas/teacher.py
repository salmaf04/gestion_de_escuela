from pydantic import BaseModel, Field
import uuid
from typing import Optional
from backend.domain.schemas.user import UserCreateModel

class TeacherModel(BaseModel):
    id : uuid.UUID
    name: str
    fullname: str
    specialty: str
    contract_type: str  
    experience: int
    email: str
    username: str
    salary: float
    list_of_subjects: list[str]
    valoration : Optional[float | str ] = None
    

class TeacherCreateModel(UserCreateModel):
    name: str
    fullname: str
    specialty: str
    contract_type: str
    experience: int
    salary: float
    list_of_subjects: list[str]
    