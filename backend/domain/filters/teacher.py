from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BooleanFilter, BaseFilter
from pydantic import BaseModel, Field
from backend.domain.models.tables import TeacherTable
from typing import Optional
import uuid
from sqlalchemy import Select
from sqlalchemy.orm import Session
from typing import Any


class TeacherAlertFilter(BaseFilter) :
    def filter(self, query: Select, value: bool, values: Any) :
        teacher_table = TeacherTable
        return query.where(
            teacher_table.less_than_three_valoration >= 5
        )
        

class TeacherFilterSet(FilterSet):
    id = Filter(TeacherTable.id)
    name = Filter(TeacherTable.name)
    email = Filter(TeacherTable.email)
    specialty = Filter(TeacherTable.specialty)
    contract_type = Filter(TeacherTable.contract_type)
    experience = RangeFilter(TeacherTable.experience)
    alert = TeacherAlertFilter()

class TeacherFilterSchema(BaseModel):
    id : uuid.UUID | None = None
    name : str | None = None
    email : str | None = None
    specialty : str | None = None
    contract_type : str | None = None
    experince : tuple[int, int] | None = None
    alert : bool | None = None
    
class TeacherChangeRequest(BaseModel) :
    name : Optional[str] = None
    full_name : Optional[str] = None
    specialty : Optional[str] = None
    contract_type : Optional[str] = None
    experience : Optional[int] = None
   