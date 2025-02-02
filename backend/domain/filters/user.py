from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BooleanFilter, InFilter
from pydantic import BaseModel
from backend.domain.models.tables import UserTable


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
    username : Optional[str] = None
    email : Optional[str] = None

class UserPasswordChangeRequest(BaseModel) :
    current_password : str | None = None
    new_password : str | None = None