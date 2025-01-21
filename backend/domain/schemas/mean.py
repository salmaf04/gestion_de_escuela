from pydantic import BaseModel
import uuid

class MeanModel (BaseModel):
    id: uuid.UUID
    name: str
    state: str
    location: str
    classroom_id: uuid.UUID
    type: str
    
class MeanCreateModel(BaseModel):
    name: str
    state: str
    location: str 
    classroom_id: uuid.UUID
    type: str


class MeanClassroomModel (BaseModel):
    id: uuid.UUID
    name: str
    state: str
    location: str
    type: str
    