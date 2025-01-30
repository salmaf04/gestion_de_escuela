from pydantic import BaseModel
import uuid
from typing import Optional

class MeanMaintenanceCreateModel(BaseModel):
    mean_id: uuid.UUID
    cost: float
    date : str
    finished : Optional[bool | None] = None

class MeanMaintenanceModel(BaseModel):
    id: uuid.UUID
    mean: str
    cost: float
    date : str
    finished : bool | None = None





    

