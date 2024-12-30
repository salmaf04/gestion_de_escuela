from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BooleanFilter
from pydantic import BaseModel, Field
from backend.domain.models.tables import TeacherTable
from typing import Optional

class TeacherFilterSet(FilterSet):
    name = Filter(TeacherTable.name)
    email = Filter(TeacherTable.email)
    specialty = Filter(TeacherTable.specialty)
    contract_type = Filter(TeacherTable.contract_type)
    experience = RangeFilter(TeacherTable.experience)

class TeacherFilterSchema(BaseModel):
    name : str | None = None
    email : str | None = None
    specialty : str | None = None
    contract_type : str | None = None
    experince : tuple[int, int] | None = None
    
class ChangeRequest(BaseModel) :
    name : Optional[str] = None
    full_name : Optional[str] = None
    specialty : Optional[str] = None
    contract_type : Optional[str] = None
    experience : Optional[int] = None
   