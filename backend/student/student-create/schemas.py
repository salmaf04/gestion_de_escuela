from pydantic import BaseModel
import uuid

class StudentCreateModel(BaseModel):
    name: str
    age: int
    extra_activities: bool

class StudentModel(BaseModel):
    id : uuid.UUID
    name: str
    age: int
    extra_activities: bool