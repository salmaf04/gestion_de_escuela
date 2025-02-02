from pydantic import BaseModel
import uuid
from backend.domain.schemas.user import UserCreateModel

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
    



