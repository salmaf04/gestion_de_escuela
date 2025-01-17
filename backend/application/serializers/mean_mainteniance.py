from backend.domain.schemas.mean_mainteniance import MeanMaintenanceModel
from backend.domain.models.tables import MeanMaintenianceTable
from pydantic import BaseModel

class MaintenanceByType(BaseModel):
    type: str
    count: int


class ClassroomMaintenance(BaseModel):
    list: list[MaintenanceByType]


class MeanMaintenanceByClassroom(BaseModel):
    classrooms : list[ClassroomMaintenance]
    

class MeanMaintenanceMapper :

    def to_api(self, mean_maintenance: MeanMaintenianceTable) -> MeanMaintenianceTable :
        return MeanMaintenanceModel(
            id = mean_maintenance.entity_id,
            mean = mean_maintenance.mean.name,
            date = mean_maintenance.date.date.strftime("%Y-%m-%d"),
            cost = mean_maintenance.cost
        )
    
 
