from pydantic import BaseModel
from typing import Optional
from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BooleanFilter
from pydantic import BaseModel
from backend.domain.models.tables import SecretaryTable

"""
This module defines filter sets and schemas for managing secretaries using SQLAlchemy and Pydantic.

Classes:
- SecretaryFilterSet: A filter set for querying secretaries based on ID, name, email, and username.
- SecretaryFilterSchema: A Pydantic model for defining the schema of secretary filters, allowing optional filtering by ID, name, email, and username.
- SecretaryChangeRequest: A Pydantic model for defining the schema of change requests for secretaries, allowing optional updates to name, username, email, and hashed password.

Dependencies:
- SQLAlchemy's FilterSet and Filter for creating query filters.
- Pydantic's BaseModel for defining data validation and serialization.
- Optional from typing for optional fields.

Attributes:
- id (str | None): The ID of the secretary to filter by.
- name (str | None): The name of the secretary to filter by or update.
- email (str | None): The email of the secretary to filter by or update.
- username (str | None): The username of the secretary to filter by or update.
- hash_password (str | None): The hashed password for updating a secretary's credentials.
"""

class SecretaryFilterSet(FilterSet):
    id = Filter(SecretaryTable.id)
    name = Filter(SecretaryTable.name)
    email = Filter(SecretaryTable.email)
    username = Filter(SecretaryTable.username)

class SecretaryFilterSchema(BaseModel):
    id : str | None = None
    name : str | None = None
    email : str | None = None
    username : str | None = None
    
class SecretaryChangeRequest(BaseModel) :
    name : Optional[str] = None
    username : Optional[str] = None
    email : Optional[str] = None
    hash_password : Optional[str] = None

