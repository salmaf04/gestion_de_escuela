from sqlalchemy_filterset import FilterSet, Filter, RangeFilter
from pydantic import BaseModel
from backend.domain.models.tables import CourseTable
from typing import Optional


class CourseFilterSet(FilterSet):
    year = Filter(CourseTable.year)

class CourseFilterSchema(BaseModel):
    year : int | None = None

class CourseChangeRequest(BaseModel) :
    year : Optional[int] = None