from sqlalchemy_filterset import FilterSet, Filter, RangeFilter
from pydantic import BaseModel
from backend.domain.models.tables import DeanTable
from typing import Optional

class DeanFilterSet(FilterSet):
    name = Filter(DeanTable.name)
    email = Filter(DeanTable.email)
    specialty = Filter(DeanTable.specialty)
    contract_type = Filter(DeanTable.contract_type)
    experience = RangeFilter(DeanTable.experience)

class DeanFilterSchema(BaseModel):
    name : str | None = None
    email : str | None = None
    specialty : str | None = None
    contract_type : str | None = None
    experince : tuple[int, int] | None = None
    
class ChangeRequest(BaseModel) :
    name : Optional[str] = None
    full_name : Optional[str] = None
    email : Optional[str] = None
    specialty : Optional[str] = None
    contract_type : Optional[str] = None
    experience : Optional[int] = None
    username : Optional[str] = None
    hash_password : Optional[str] = None