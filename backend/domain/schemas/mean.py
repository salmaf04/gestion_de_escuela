from pydantic import BaseModel
import uuid

class MeanModel (BaseModel):
    id: uuid.UUID
    name: str
    state: str
    location: str
    
class MeanCreateModel(BaseModel):
    name: str
    state: str
    location: str 