from sqlalchemy_filterset import FilterSet, Filter, InFilter
from pydantic import BaseModel
from backend.domain.models.tables import MeanTable
from typing import Optional


class MeanFilterSet(FilterSet):
    name = Filter(MeanTable.name)
    state = InFilter(MeanTable.state)
    location = Filter(MeanTable.location)
    type = Filter(MeanTable.type)

class MeanFilterSchema(BaseModel):
    name : str | None = None
    state : list[str] | None = None
    location : str | None = None
    type : str | None = None
    
class ChangeRequest(BaseModel) :
    state : Optional[str] = None
    location : Optional[str] = None