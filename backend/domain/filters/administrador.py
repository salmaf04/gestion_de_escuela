from pydantic import BaseModel
from typing import Optional
from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BooleanFilter
from pydantic import BaseModel
from backend.domain.models.tables import AdministratorTable

"""
This module defines filter sets and schemas for managing administrators using SQLAlchemy and Pydantic.

Classes:
- AdministratorFilterSet: A filter set for querying administrators based on ID, name, email, and username.
- AdministratorFilterSchema: A Pydantic model for defining the schema of administrator filters, allowing optional filtering by ID, name, email, and username.
- AdministratorChangeRequest: A Pydantic model for defining the schema of change requests for administrators, allowing optional updates to name, username, email, and hashed password.

Dependencies:
- SQLAlchemy's FilterSet and Filter for creating query filters.
- Pydantic's BaseModel for defining data validation and serialization.
- Optional from typing for optional fields.

Attributes:
- id (str | None): The ID of the administrator to filter by.
- name (str | None): The name of the administrator to filter by.
- email (str | None): The email of the administrator to filter by.
- username (str | None): The username of the administrator to filter by.
- hash_password (str | None): The hashed password for updating an administrator's credentials.
"""
class AdministratorFilterSet(FilterSet):
    id = Filter(AdministratorTable.id)
    name = Filter(AdministratorTable.name)
    email = Filter(AdministratorTable.email)
    username = Filter(AdministratorTable.username)

class AdministratorFilterSchema(BaseModel):
    id : str | None = None
    name : str | None = None
    email : str | None = None    
    username : str | None = None

class AdministratorChangeRequest(BaseModel) :
    name : Optional[str] = None
    lastname : Optional[str] = None
    username : Optional[str] = None
    email : Optional[str] = None
    hash_password : Optional[str] = None
