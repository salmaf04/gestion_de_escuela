from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BooleanFilter, InFilter
from pydantic import BaseModel
from backend.domain.models.tables import SubjectTable
from typing import Optional


class SubjectFilterSet(FilterSet):
    name = InFilter(SubjectTable.name)
    hourly_load = RangeFilter(SubjectTable.hourly_load)
    study_program = RangeFilter(SubjectTable.study_program)

class SubjectFilterSchema(BaseModel):
    name : list[str] | None = None
    hourly_load : tuple[int, int] | None = None
    study_program : tuple[int, int] | None = None

class SubjectChangeRequest(BaseModel) :
    name : Optional[str] = None
    hourly_load : Optional[int] = None
    study_program : Optional[int] = None
    classroom_id : Optional[str] = None