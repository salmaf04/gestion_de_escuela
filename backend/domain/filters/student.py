from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BooleanFilter
from pydantic import BaseModel
from backend.domain.models.tables import StudentTable
from typing import Optional


class StudentFilterSet(FilterSet):
    name = Filter(StudentTable.name)
    age = RangeFilter(StudentTable.age)
    email = Filter(StudentTable.email)
    extra_activities = BooleanFilter(StudentTable.extra_activities)

class StudentFilterSchema(BaseModel):
    name : str | None = None
    age : tuple[int, int] | None = None
    email : str | None = None
    extra_activities : bool | None = None

class ChangeRequest(BaseModel) :
    name : Optional[str] = None
    age : Optional[int] = None
    email : Optional[str] = None
    extra_activities : Optional[bool] = None
    username : Optional[str] = None
    hash_password : Optional[str] = None