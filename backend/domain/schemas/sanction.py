from pydantic import BaseModel
import uuid
from datetime import datetime

class SanctionCreateModel(BaseModel):
    amount: float
    teacher_id : uuid.UUID
    date : datetime

class SanctionModel(SanctionCreateModel):
    id : uuid.UUID