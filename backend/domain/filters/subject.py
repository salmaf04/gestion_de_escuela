from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BooleanFilter
from pydantic import BaseModel
from backend.domain.models.tables import SubjectTable
from typing import Optional


class SubjectFilterSet(FilterSet):
    name = Filter(SubjectTable.name)
    hourly_load = RangeFilter(SubjectTable.hourly_load)
    study_program = RangeFilter(SubjectTable.study_program)

class SubjectFilterSchema(BaseModel):
    name : str | None = None
    hourly_load : tuple[int, int] | None = None
    study_program : tuple[int, int] | None = None

class ChangeRequest(BaseModel) :
    name : Optional[str] = None
    hourly_load : Optional[int] = None
    study_program : Optional[int] = None