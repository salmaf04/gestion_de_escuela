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
    password: str

class StudentSubjectPerformance(BaseModel):
    subject_id : uuid.UUID
    average_subject_performance : float

class StudentAcademicPerformance(BaseModel):
    id : uuid.UUID
    performance : list[StudentSubjectPerformance]



