from sqlalchemy_filterset import FilterSet, Filter, RangeFilter
from pydantic import BaseModel
from backend.domain.models.tables import MeanMaintenianceTable
from typing import Optional
import uuid


class MeanMaintenanceFilterSet(FilterSet):
    mean_id = Filter(MeanMaintenianceTable.mean_id)
    date_id = Filter(MeanMaintenianceTable.date_id)
    cost = Filter(MeanMaintenianceTable.cost)


class MeanMaintenanceFilterSchema(BaseModel):
    mean_id : uuid.UUID | None = None
    date_id : uuid.UUID | None = None
    cost : float| None = None