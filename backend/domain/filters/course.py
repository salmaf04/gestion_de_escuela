from sqlalchemy_filterset import FilterSet, Filter, RangeFilter
from pydantic import BaseModel
from backend.domain.models.tables import CourseTable
from typing import Optional


class CourseFilterSet(FilterSet):
    start_date = RangeFilter(CourseTable.start_date)
    end_date = RangeFilter(CourseTable.end_date)

class CourseFilterSchema(BaseModel):
    start_date : tuple[int, int] | None = None
    end_date : tuple[int, int] | None = None

class ChangeRequest(BaseModel) :
    start_date : Optional[int] = None
    end_date : Optional[int] = None