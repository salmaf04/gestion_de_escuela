from pydantic import BaseModel
import uuid

class MeanMaintenanceCreateModel(BaseModel):
    mean_id: uuid.UUID
    date_id: uuid.UUID
    cost: float

class MeanMaintenanceModel(BaseModel):
    id: uuid.UUID
    mean: str
    date: str
    cost: float





    

