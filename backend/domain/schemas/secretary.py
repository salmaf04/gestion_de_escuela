from pydantic import BaseModel
import uuid
from backend.domain.schemas.user import UserCreateModel

"""
This module defines Pydantic models for representing secretary data in the application.

Classes:
    SecretaryModel: A model representing a secretary with detailed attributes.
    SecretaryCreateModel: A model for creating new secretary records, extending user creation attributes.

Class Details:

1. SecretaryModel:
    - Inherits from Pydantic's BaseModel.
    - Represents a secretary with detailed attributes.
    - Attributes:
        - id: The unique identifier of the secretary (UUID).
        - name: The first name of the secretary (string).
        - lastname: The last name of the secretary (string).
        - username: The username of the secretary (string).
        - email: The email address of the secretary (string).
        - hash_password: The hashed password of the secretary (string).

2. SecretaryCreateModel:
    - Inherits from UserCreateModel.
    - Represents the data required to create a new secretary, including user creation attributes.
    - This class does not add any new attributes beyond those in UserCreateModel.

Dependencies:
    - Pydantic for data validation and serialization.
    - UUID for handling unique identifiers.
    - UserCreateModel for user-related attributes during secretary creation.
"""

class SecretaryModel(BaseModel):
    id : uuid.UUID
    name: str
    lastname: str
    username: str
    email: str
    hash_password: str
    
class SecretaryCreateModel(UserCreateModel):
    pass