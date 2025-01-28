from pydantic import BaseModel
import uuid

class SubjectModel(BaseModel):
    id : uuid.UUID
    name: str
    hourly_load: int
    study_program: int
    classroom_id : uuid.UUID
    course_id : uuid.UUID   
    
class SubjectCreateModel(BaseModel):
    name: str
    hourly_load: int
    study_program: int
    classroom_id : uuid.UUID
    course_id : uuid.UUID