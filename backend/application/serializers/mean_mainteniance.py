from backend.domain.schemas.mean_mainteniance import MeanMaintenanceModel
from backend.domain.models.tables import MeanMaintenianceTable

class MeanMaintenanceMapper :

    def to_api(self, mean_maintenance: MeanMaintenianceTable) -> MeanMaintenianceTable :
        return MeanMaintenanceModel(
            id = mean_maintenance.entity_id,
            mean_id = mean_maintenance.mean_id,
            date_id = mean_maintenance.date_id,
            cost = mean_maintenance.cost
        )