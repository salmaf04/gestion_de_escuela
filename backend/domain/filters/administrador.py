from pydantic import BaseModel
from typing import Optional
from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BooleanFilter
from pydantic import BaseModel
from backend.domain.models.tables import AdministratorTable

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
    username : Optional[str] = None
    email : Optional[str] = None
    hash_password : Optional[str] = None
