from sqlalchemy_filterset import FilterSet, Filter, RangeFilter
from pydantic import BaseModel
from backend.domain.models.tables import CourseTable
from typing import Optional

"""
This module defines filter sets and schemas for managing courses using SQLAlchemy and Pydantic.

Classes:
- CourseFilterSet: A filter set for querying courses based on the year.
- CourseFilterSchema: A Pydantic model for defining the schema of course filters, allowing optional filtering by year.
- CourseChangeRequest: A Pydantic model for defining the schema of change requests for courses, allowing optional updates to the year.

Dependencies:
- SQLAlchemy's FilterSet and Filter for creating query filters.
- Pydantic's BaseModel for defining data validation and serialization.
- Optional from typing for optional fields.

Attributes:
- year (int | None): The year of the course to filter by or update.
"""

class CourseFilterSet(FilterSet):
    year = Filter(CourseTable.year)

class CourseFilterSchema(BaseModel):
    year : int | None = None

class CourseChangeRequest(BaseModel) :
    year : Optional[int] = None