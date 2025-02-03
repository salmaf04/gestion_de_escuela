from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BooleanFilter, InFilter
from pydantic import BaseModel
from backend.domain.models.tables import SubjectTable
from typing import Optional

"""
This module defines filter sets and schemas for managing subjects using SQLAlchemy and Pydantic.

Classes:
- SubjectFilterSet: A filter set for querying subjects based on name, hourly load, study program, and course ID.
- SubjectFilterSchema: A Pydantic model for defining the schema of subject filters, allowing optional filtering by name, hourly load range, study program range, and course ID.
- SubjectChangeRequest: A Pydantic model for defining the schema of change requests for subjects, allowing optional updates to various attributes.

Dependencies:
- SQLAlchemy's FilterSet, InFilter, RangeFilter, and Filter for creating query filters.
- Pydantic's BaseModel for defining data validation and serialization.
- Optional from typing for optional fields.

Attributes:
- name (list[str] | None): The names of the subjects to filter by.
- hourly_load (tuple[int, int] | int | None): The hourly load range to filter by or the hourly load to update.
- study_program (tuple[int, int] | int | None): The study program range to filter by or the study program to update.
- course_id (str | None): The course ID to filter by.
- classroom_id (str | None): The classroom ID to update.
"""

class SubjectFilterSet(FilterSet):
    name = InFilter(SubjectTable.name)
    hourly_load = RangeFilter(SubjectTable.hourly_load)
    study_program = RangeFilter(SubjectTable.study_program)
    course_id = Filter(SubjectTable.course_id)

class SubjectFilterSchema(BaseModel):
    name : list[str] | None = None
    hourly_load : tuple[int, int] | None = None
    study_program : tuple[int, int] | None = None
    course_id : str | None = None

class SubjectChangeRequest(BaseModel) :
    name : Optional[str] = None
    hourly_load : Optional[int] = None
    study_program : Optional[int] = None
    classroom_id : Optional[str] = None