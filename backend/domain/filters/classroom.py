"""
Filter classes for classroom-related queries using SQLAlchemy-FilterSet.
These filters help in querying and filtering classroom data based on various criteria.
"""

from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BaseFilter
from pydantic import BaseModel
from backend.domain.models.tables import ClassroomTable, teacher_request_classroom_table
from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import Any
from sqlalchemy import Select

class AvaliableClassroomFilter(BaseFilter):
    """
    Custom filter for finding available classrooms.
    Filters out classrooms that are currently requested by teachers.
    
    Returns:
        Query filtered to show only classrooms that are not in the teacher_request_classroom table.
    """
    def filter(self, query: Select, value: bool, values: Any) -> list[ClassroomTable]:
        classroom_table = ClassroomTable

        return query.where(
            classroom_table.entity_id.notin_(
                select(teacher_request_classroom_table.c.classroom_id)
            )
        )

class ClassroomFilterSet(FilterSet):
    """
    Collection of filters for classroom queries.
    Attributes:
        - number: Filter by classroom number
        - location: Filter by classroom location
        - capacity: Range filter for classroom capacity
        - avaliable: Filter for classroom availability
    """
    number = Filter(ClassroomTable.number)
    location = Filter(ClassroomTable.location)
    capacity = RangeFilter(ClassroomTable.capacity)
    avaliable = AvaliableClassroomFilter()
        
class ClassroomFilterSchema(BaseModel):
    """
    Pydantic model defining the schema for classroom filtering parameters.
    All fields are optional to allow partial filtering.
    Attributes:
        - number: Optional classroom number
        - location: Optional classroom location
        - capacity: Optional tuple of (min, max) capacity
        - avaliable: Optional boolean for availability
    """
    number: int | None = None
    location: str | None = None
    capacity: tuple[int, int] | None = None
    avaliable: Optional[bool] = None

class ClassroomChangeRequest(BaseModel):
    """
    Pydantic model for classroom modification requests.
    All fields are optional to allow partial updates.
    Attributes:
        - number: Optional new classroom number
        - location: Optional new location
        - capacity: Optional new capacity
    """
    number: Optional[int] = None
    location: Optional[str] = None
    capacity: Optional[int] = None