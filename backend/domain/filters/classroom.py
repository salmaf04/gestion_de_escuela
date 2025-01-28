from sqlalchemy_filterset import FilterSet, Filter, RangeFilter
from pydantic import BaseModel
from backend.domain.models.tables import ClassroomTable
from typing import Optional


class ClassroomFilterSet(FilterSet):
    location = Filter(ClassroomTable.location)
    capacity = RangeFilter(ClassroomTable.capacity)
    
    
class ClassroomFilterSchema(BaseModel):
    location : str | None = None
    capacity : tuple[int, int] | None = None

class ClassroomChangeRequest(BaseModel) :
    location : Optional[str] = None
    capacity : Optional[int] = None