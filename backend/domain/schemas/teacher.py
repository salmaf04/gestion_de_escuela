from pydantic import BaseModel
import uuid

class TeacherModel(BaseModel):
    id : uuid.UUID
    name: str
    fullname: str
    specialty: str
    contract_type: str  
    experience: int
    email: str
    username: str
    list_of_subjects: list[str]
    

class TeacherCreateModel(BaseModel):
    name: str
    fullname: str
    email: str
    specialty: str
    contract_type: str
    experience: int
    username: str
    password: str
    list_of_subjects: list[str]