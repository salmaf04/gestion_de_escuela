from backend.domain.schemas.mean_mainteniance import MeanMaintenanceModel
from backend.domain.models.tables import MeanMaintenianceTable

class MeanMaintenanceMapper :

    def to_api(self, mean_maintenance: MeanMaintenianceTable) -> MeanMaintenianceTable :
        return MeanMaintenanceModel(
            id = mean_maintenance.entity_id,
            mean = mean_maintenance.mean.name,
            date = mean_maintenance.date.date.strftime("%Y-%m-%d"),
            cost = mean_maintenance.cost
        )