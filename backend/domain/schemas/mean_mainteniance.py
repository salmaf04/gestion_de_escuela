from pydantic import BaseModel
import uuid

class MeanMaintenanceCreateModel(BaseModel):
    mean_id: uuid.UUID
    cost: float
    date : str

class MeanMaintenanceModel(BaseModel):
    id: uuid.UUID
    mean: str
    cost: float
    date : str





    

