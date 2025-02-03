from pydantic import BaseModel
import uuid
from datetime import datetime

"""
This module defines Pydantic models for representing sanction data in the application.

Classes:
    SanctionCreateModel: A model for creating new sanction records.
    SanctionModel: A model representing a sanction record with additional attributes.

Class Details:

1. SanctionCreateModel:
    - Inherits from Pydantic's BaseModel.
    - Represents the data required to create a new sanction record.
    - Attributes:
        - amount: The amount of the sanction (float).
        - teacher_id: The unique identifier of the teacher associated with the sanction (UUID).
        - date: The date of the sanction (datetime).

2. SanctionModel:
    - Inherits from SanctionCreateModel.
    - Represents a sanction record with additional attributes.
    - Attributes:
        - id: The unique identifier of the sanction record (UUID).

Dependencies:
    - Pydantic for data validation and serialization.
    - UUID for handling unique identifiers.
    - datetime for handling date and time values.
"""
class SanctionCreateModel(BaseModel):
    amount: float
    teacher_id : uuid.UUID
    date : datetime

class SanctionModel(SanctionCreateModel):
    id : uuid.UUID