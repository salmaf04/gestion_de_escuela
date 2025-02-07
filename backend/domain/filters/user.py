from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BooleanFilter, InFilter
from pydantic import BaseModel
from backend.domain.models.tables import UserTable

"""
This module defines filter sets and schemas for managing users using SQLAlchemy and Pydantic.

Classes:
- UserFilterSet: A filter set for querying users based on ID, username, email, name, lastname, type, and roles.
- UserFilterSchema: A Pydantic model for defining the schema of user filters, allowing optional filtering by various attributes.
- UserChangeRequest: A Pydantic model for defining the schema of change requests for users, allowing optional updates to username and email.
- UserPasswordChangeRequest: A Pydantic model for defining the schema of password change requests for users, allowing updates to current and new passwords.

Dependencies:
- SQLAlchemy's FilterSet, Filter, and InFilter for creating query filters.
- Pydantic's BaseModel for defining data validation and serialization.
- Optional from typing for optional fields.

Attributes:
- id (str | None): The ID of the user to filter by.
- username (str | None): The username of the user to filter by or update.
- email (str | None): The email of the user to filter by or update.
- name (str | None): The name of the user to filter by.
- lastname (str | None): The lastname of the user to filter by.
- type (str | None): The type of the user to filter by.
- roles (list[str] | None): The roles of the user to filter by.
- current_password (str | None): The current password for updating a user's credentials.
- new_password (str | None): The new password for updating a user's credentials.
"""
class UserFilterSet(FilterSet):
    id = Filter(UserTable.entity_id)
    username = Filter(UserTable.username)
    email = Filter(UserTable.email)
    name = Filter(UserTable.name)
    lastname = Filter(UserTable.lastname)
    type = Filter(UserTable.type)
    roles = InFilter(UserTable.roles)

class UserFilterSchema(BaseModel):
    id : str | None = None
    username : str | None = None
    email : str | None = None
    name : str | None = None
    lastname : str | None = None
    type : str | None = None
    roles : list[str] | None = None
class UserChangeRequest(BaseModel) :
    name : Optional[str] = None
    lastname : Optional[str] = None
    username : Optional[str] = None
    email : Optional[str] = None

class UserPasswordChangeRequest(BaseModel) :
    current_password : str | None = None
    new_password : str | None = None