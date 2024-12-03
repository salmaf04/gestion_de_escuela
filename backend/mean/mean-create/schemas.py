from pydantic import BaseModel
import uuid

class MeanCreateModel(BaseModel):
    name: str
    state: str
    location: str 


class MeanModel(BaseModel):
    id: uuid.UUID
    name: str
    state: str
    location: str 