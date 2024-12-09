from pydantic import BaseModel
import uuid

class StudentModel(BaseModel):
    id : uuid.UUID
    name: str
    hourly_load: int
    study_program: int
    
class StudentCreateModel(BaseModel):
    name: str
    hourly_load: int
    study_program: int