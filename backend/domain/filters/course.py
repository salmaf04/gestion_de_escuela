from sqlalchemy_filterset import FilterSet, Filter, RangeFilter
from pydantic import BaseModel
from backend.domain.models.tables import CourseTable
from typing import Optional


class CourseFilterSet(FilterSet):
    start_year = RangeFilter(CourseTable.start_year)
    end_year = RangeFilter(CourseTable.end_year)

class CourseFilterSchema(BaseModel):
    start_year : tuple[int, int] | None = None
    end_year : tuple[int, int] | None = None

class ChangeRequest(BaseModel) :
    start_year : Optional[int] = None
    end_year : Optional[int] = None