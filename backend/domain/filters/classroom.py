from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BaseFilter
from pydantic import BaseModel
from backend.domain.models.tables import ClassroomTable, teacher_request_classroom_table
from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import Any
from sqlalchemy import Select

class AvaliableClassroomFilter(BaseFilter) :
    def filter(self, query: Select, value: bool, values: Any) -> list[ClassroomTable] :
        classroom_table = ClassroomTable

        return query.where(
            classroom_table.entity_id.notin_(
                select(teacher_request_classroom_table.c.classroom_id)
            )
        )

class ClassroomFilterSet(FilterSet):
    location = Filter(ClassroomTable.location)
    capacity = RangeFilter(ClassroomTable.capacity)
    avaliable = AvaliableClassroomFilter()
        
class ClassroomFilterSchema(BaseModel):
    location : str | None = None
    capacity : tuple[int, int] | None = None
    avaliable : Optional[bool] = None

class ClassroomChangeRequest(BaseModel) :
    location : Optional[str] = None
    capacity : Optional[int] = None