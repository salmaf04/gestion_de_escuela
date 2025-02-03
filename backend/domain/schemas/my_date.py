from pydantic import BaseModel
from datetime import datetime
import uuid

"""
This module defines Pydantic models for representing date-related data in the application.

Classes:
    DateModel: A model representing a date record with an identifier.
    DateCreateModel: A model for creating new date records.

Class Details:

1. DateModel:
    - Inherits from Pydantic's BaseModel.
    - Represents a date record with an identifier.
    - Attributes:
        - id: The unique identifier of the date record (UUID).
        - date: The date value (datetime).

2. DateCreateModel:
    - Inherits from Pydantic's BaseModel.
    - Represents the data required to create a new date record.
    - Attributes:
        - date: The date value (datetime).

Dependencies:
    - Pydantic for data validation and serialization.
    - UUID for handling unique identifiers.
    - datetime for handling date and time values.
"""

class DateModel (BaseModel):
    id: uuid.UUID
    date: datetime
    
class DateCreateModel(BaseModel):
    date: datetime