from pydantic import BaseModel
import uuid

class StudentModel(BaseModel):
    id : uuid.UUID
    name: str
    age: int
    email: str
    extra_activities: bool
    username: str
    hash_password: str
    
class StudentCreateModel(BaseModel):
    name: str
    age: int
    email: str
    extra_activities: bool
    username: str
    hash_password: str
