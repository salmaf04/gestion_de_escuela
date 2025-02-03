from pydantic import BaseModel
import uuid
from backend.domain.schemas.user import UserCreateModel

"""
This module defines Pydantic models for representing dean data in the application.

Classes:
    DeanModel: A model representing a dean with detailed attributes.
    DeanCreateModel: A model for creating new dean records, extending user creation attributes.

Class Details:

1. DeanModel:
    - Inherits from Pydantic's BaseModel.
    - Represents a dean with detailed attributes.
    - Attributes:
        - id: The unique identifier of the dean (UUID).
        - name: The first name of the dean (string).
        - lastname: The last name of the dean (string).
        - specialty: The specialty of the dean (string).
        - contract_type: The type of contract the dean has (string).
        - experience: The number of years of experience the dean has (integer).
        - email: The email address of the dean (string).
        - username: The username of the dean (string).

2. DeanCreateModel:
    - Inherits from UserCreateModel.
    - Represents the data required to create a new dean, including user creation attributes.
    - Attributes:
        - specialty: The specialty of the dean (string).
        - contract_type: The type of contract the dean has (string).
        - experience: The number of years of experience the dean has (integer).

Dependencies:
    - Pydantic for data validation and serialization.
    - UUID for handling unique identifiers.
    - UserCreateModel for user-related attributes during dean creation.
"""

class DeanModel(BaseModel):
    id : uuid.UUID
    name: str
    lastname: str
    lastname: str
    specialty: str
    contract_type: str  
    experience: int
    email: str
    username: str
    

class DeanCreateModel(UserCreateModel):
    specialty: str
    contract_type: str
    experience: int