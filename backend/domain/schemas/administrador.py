"""
Pydantic models for administrator data validation and serialization.
These models define the structure for creating and representing administrator data.
"""

from pydantic import BaseModel
import uuid
from backend.domain.schemas.user import UserCreateModel

class AdministratorCreateModel(UserCreateModel):
    """
    Pydantic model for creating a new administrator.
    Inherits all fields from UserCreateModel without adding additional fields:
        - name: administrator's first name
        - lastname: administrator's last name
        - username: unique username
        - email: administrator's email
        - password: administrator's password (will be hashed)
    """
    pass


class AdministratorModel(BaseModel):
    """
    Pydantic model for representing an administrator.
    Used for responses and data serialization.
    Attributes:
        - id: UUID identifier for the administrator
        - name: administrator's first name
        - lastname: administrator's last name
        - username: unique username
        - email: administrator's email
        - hash_password: administrator's hashed password
    """
    id: uuid.UUID
    name: str
    lastname: str
    username: str
    email: str
    hash_password: str

