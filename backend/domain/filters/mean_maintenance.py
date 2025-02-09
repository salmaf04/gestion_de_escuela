from sqlalchemy_filterset import FilterSet, Filter, RangeFilter
from pydantic import BaseModel
from backend.domain.models.tables import MeanMaintenanceTable
from typing import Optional
import uuid

"""
This module defines filter sets and schemas for managing mean maintenance records using SQLAlchemy and Pydantic.

Classes:
- MeanMaintenanceFilterSet: A filter set for querying mean maintenance records based on mean ID, cost, and finished status.
- MeanMaintenanceFilterSchema: A Pydantic model for defining the schema of mean maintenance filters, allowing optional filtering by mean ID, cost, and finished status.
- MeanMaintenanceChangeRequest: A Pydantic model for defining the schema of change requests for mean maintenance records, allowing optional updates to the finished status.

Dependencies:
- SQLAlchemy's FilterSet and Filter for creating query filters.
- Pydantic's BaseModel for defining data validation and serialization.
- UUID for handling unique identifiers.
- Optional from typing for optional fields.

Attributes:
- mean_id (uuid.UUID | None): The ID of the mean to filter by.
- cost (float | None): The cost of the maintenance to filter by.
- finished (bool | None): The finished status to filter by or update.
"""

class MeanMaintenanceFilterSet(FilterSet):
    id = Filter(MeanMaintenanceTable.entity_id)
    mean_id = Filter(MeanMaintenanceTable.mean_id)
    cost = Filter(MeanMaintenanceTable.cost)
    finished = Filter(MeanMaintenanceTable.finished)


class MeanMaintenanceFilterSchema(BaseModel):
    id : uuid.UUID | None = None
    mean_id : uuid.UUID | None = None
    cost : float| None = None
    finished : bool | None = None

class MeanMaintenanceChangeRequest(BaseModel):
    cost : float | None = None
    finished : bool | None = None