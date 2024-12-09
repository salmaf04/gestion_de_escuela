from pydantic import BaseModel
from datetime import datetime
import uuid

class DateModel (BaseModel):
    id: uuid.UUID
    date: datetime
    
class DateCreateModel(BaseModel):
    date: datetime