from pydantic import BaseModel
from typing import Optional
from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BooleanFilter
from pydantic import BaseModel
from backend.domain.models.tables import SecretaryTable

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

