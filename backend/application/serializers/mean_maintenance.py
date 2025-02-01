from backend.domain.schemas.mean_maintenance import MeanMaintenanceModel
from backend.domain.models.tables import MeanMaintenanceTable
from pydantic import BaseModel
import uuid

class MaintenanceByType(BaseModel):
    type: str
    count: int


class ClassroomMaintenance(BaseModel):
    list: list[MaintenanceByType]


class MeanMaintenanceByClassroom(BaseModel):
    classrooms : list[ClassroomMaintenance]


class MeanMaintenanceDate(BaseModel):
    average_cost: float
    mean_id: uuid.UUID
    mean_name: str


class MeanMaintenanceClassroom(BaseModel) :
    number : int = 0
    other : int = 0
    teaching_material : int = 0
    technological_mean : int = 0
    total_after_two_years : int = 0
    

class MeanMaintenanceMapper :

    def to_api(self, mean_maintenance: MeanMaintenanceTable) -> MeanMaintenanceTable :
        return MeanMaintenanceModel(
            id = mean_maintenance.entity_id,
            mean = mean_maintenance.mean.name,
            cost = mean_maintenance.cost,
            date = mean_maintenance.date.strftime("%d-%m-%Y"),
            finished = mean_maintenance.finished
        )
    

    def to_date(self, data) :
        serialized_values = []

        for mean_maintenance in data :
            new_mean_maintenance = MeanMaintenanceDate(
                average_cost = mean_maintenance[2],
                mean_id = mean_maintenance[0],
                mean_name = mean_maintenance[1]
            )

            serialized_values.append(new_mean_maintenance)

        return serialized_values
    

    def to_classroom(self, data1, data2) :
        serialized_values = []
        classroom_ids = []

        for classroom in data1 :
            if classroom[1] in classroom_ids :
                if classroom[0] == "technological_mean" :
                    serialized_values[len(serialized_values)-1].technological_mean = classroom[2]
                elif classroom[0] == "teaching_material" :
                    serialized_values[len(serialized_values)-1].teaching_material = classroom[2]
                else :
                    serialized_values[len(serialized_values)-1].other = classroom[2]
            else :
                classroom_ids.append(classroom[1])

                new_classroom = MeanMaintenanceClassroom(
                    number= classroom[1],
                    other = classroom[2] if classroom[0] == "other" else 0,
                    teaching_material = classroom[2] if classroom[0] == "teaching_material" else 0,
                    technological_mean = classroom[2] if classroom[0] == "technological_mean" else 0,
                    total_after_two_years = 0
                )
                serialized_values.append(new_classroom)

            for mapped_classroom, total in zip(serialized_values, data2) :
                mapped_classroom.total_after_two_years = total[1]

        return serialized_values
    
 
