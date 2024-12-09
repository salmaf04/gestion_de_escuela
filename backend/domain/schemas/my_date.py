from pydantic import BaseModel
from datetime import datetime
import uuid

class DateModel (BaseModel):
    date: datetime
    
class DateCreateModel(BaseModel):
    id: uuid.UUID
    date: datetime