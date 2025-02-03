from sqlalchemy_filterset import FilterSet, Filter, InFilter, BooleanFilter
from pydantic import BaseModel
from backend.domain.models.tables import MeanTable
from typing import Optional

"""
This module defines filter sets and schemas for managing means using SQLAlchemy and Pydantic.

Classes:
- MeanFilterSet: A filter set for querying means based on name, state, location, replacement status, and type.
- MeanFilterSchema: A Pydantic model for defining the schema of mean filters, allowing optional filtering by name, state, location, replacement status, and type.
- MeanChangeRequest: A Pydantic model for defining the schema of change requests for means, allowing optional updates to state, location, and classroom ID.

Dependencies:
- SQLAlchemy's FilterSet, Filter, InFilter, and BooleanFilter for creating query filters.
- Pydantic's BaseModel for defining data validation and serialization.
- Optional from typing for optional fields.

Attributes:
- name (str | None): The name of the mean to filter by.
- state (list[str] | None): The state(s) of the mean to filter by.
- location (str | None): The location of the mean to filter by or update.
- to_be_replaced (bool | None): The replacement status to filter by.
- type (str | None): The type of the mean to filter by.
- classroom_id (str | None): The classroom ID to update.
"""

class MeanFilterSet(FilterSet):
    name = Filter(MeanTable.name)
    state = InFilter(MeanTable.state)
    location = Filter(MeanTable.location)
    to_be_replaced = BooleanFilter(MeanTable.to_be_replaced)
    type = Filter(MeanTable.type)

class MeanFilterSchema(BaseModel):
    name : str | None = None
    state : list[str] | None = None
    location : str | None = None
    to_be_replaced : bool | None = None
    type : str | None = None
    
class MeanChangeRequest(BaseModel) :
    state : Optional[str] = None
    location : Optional[str] = None
    classroom_id : Optional[str] = None