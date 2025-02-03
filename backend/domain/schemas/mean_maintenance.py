from pydantic import BaseModel
import uuid
from typing import Optional

"""
This module defines Pydantic models for representing mean maintenance data in the application.

Classes:
    MeanMaintenanceCreateModel: A model for creating new mean maintenance records.
    MeanMaintenanceModel: A model representing a mean maintenance record with detailed attributes.

Class Details:

1. MeanMaintenanceCreateModel:
    - Inherits from Pydantic's BaseModel.
    - Represents the data required to create a new mean maintenance record.
    - Attributes:
        - mean_id: The unique identifier of the mean (UUID).
        - cost: The cost associated with the maintenance (float).
        - date: The date of the maintenance (string).
        - finished: An optional boolean indicating whether the maintenance is finished (default is None).

2. MeanMaintenanceModel:
    - Inherits from Pydantic's BaseModel.
    - Represents a mean maintenance record with detailed attributes.
    - Attributes:
        - id: The unique identifier of the maintenance record (UUID).
        - mean: The name of the mean (string).
        - cost: The cost associated with the maintenance (float).
        - date: The date of the maintenance (string).
        - finished: An optional boolean indicating whether the maintenance is finished (default is None).

Dependencies:
    - Pydantic for data validation and serialization.
    - UUID for handling unique identifiers.
    - Optional for handling optional fields.
"""
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





    

