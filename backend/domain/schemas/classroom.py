from pydantic import BaseModel
import uuid

class ClassroomCreateModel(BaseModel):
    location : str
    capacity : int

class ClassroomModel(ClassroomCreateModel):
    id: uuid.UUID
    