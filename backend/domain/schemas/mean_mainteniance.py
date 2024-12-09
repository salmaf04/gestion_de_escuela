from pydantic import BaseModel
import uuid

class MeanMaintenanceCreateModel(BaseModel):
    mean_id: uuid.UUID
    date_id: uuid.UUID
    cost: float

class MeanMaintenanceModel(MeanMaintenanceCreateModel):
    id: uuid.UUID