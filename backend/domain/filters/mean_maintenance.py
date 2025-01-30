from sqlalchemy_filterset import FilterSet, Filter, RangeFilter
from pydantic import BaseModel
from backend.domain.models.tables import MeanMaintenanceTable
from typing import Optional
import uuid


class MeanMaintenanceFilterSet(FilterSet):
    mean_id = Filter(MeanMaintenanceTable.mean_id)
    cost = Filter(MeanMaintenanceTable.cost)


class MeanMaintenanceFilterSchema(BaseModel):
    mean_id : uuid.UUID | None = None
    cost : float| None = None