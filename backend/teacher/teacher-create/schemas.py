from pydantic import BaseModel
import uuid

class TeacherCreateModel(BaseModel):
    name: str
    fullname: str
    email: str
    specialty: str
    contract_type: str
    experience: int
    username: str
    hash_password: str

class TeacherModel(BaseModel):
    id : uuid.UUID
    name: str
    fullname: str
    email: str
    specialty: str
    contract_type: str
    experience: int
    username: str
    hash_password: str