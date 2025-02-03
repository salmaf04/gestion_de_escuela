from backend.domain.schemas.mean_maintenance import MeanMaintenanceModel
from backend.domain.models.tables import MeanMaintenanceTable
from pydantic import BaseModel
import uuid

"""
This module defines a mapper for converting mean maintenance data into various API representations.

Classes:
    MaintenanceByType: A Pydantic model representing maintenance count by type.
    ClassroomMaintenance: A Pydantic model representing a list of maintenance by type.
    MeanMaintenanceByClassroom: A Pydantic model representing maintenance data by classroom.
    MeanMaintenanceDate: A Pydantic model representing mean maintenance data with average cost and mean details.
    MeanMaintenanceClassroom: A Pydantic model representing maintenance data for a classroom with various mean types.
    MeanMaintenanceMapper: A utility class for mapping MeanMaintenanceTable objects to various API models.

Class Details:

1. MaintenanceByType:
    - Represents maintenance count by type.
    - Attributes:
        - type: The type of maintenance.
        - count: The count of maintenance occurrences.

2. ClassroomMaintenance:
    - Represents a list of maintenance by type.
    - Attributes:
        - list: A list of MaintenanceByType objects.

3. MeanMaintenanceByClassroom:
    - Represents maintenance data by classroom.
    - Attributes:
        - classrooms: A list of ClassroomMaintenance objects.

4. MeanMaintenanceDate:
    - Represents mean maintenance data with average cost and mean details.
    - Attributes:
        - average_cost: The average cost of maintenance.
        - mean_id: The unique identifier of the mean.
        - mean_name: The name of the mean.

5. MeanMaintenanceClassroom:
    - Represents maintenance data for a classroom with various mean types.
    - Attributes:
        - number: The classroom number.
        - other: Count of other types of maintenance.
        - teaching_material: Count of teaching material maintenance.
        - technological_mean: Count of technological mean maintenance.
        - total_after_two_years: Total maintenance count after two years.

6. MeanMaintenanceMapper:
    - Provides methods to convert MeanMaintenanceTable objects into various API models.
    
    Methods:
        - to_api(mean_maintenance: MeanMaintenanceTable) -> MeanMaintenanceModel: 
            Converts a MeanMaintenanceTable object into a MeanMaintenanceModel object.
        - to_date(data): 
            Converts raw data into a list of MeanMaintenanceDate objects.
        - to_classroom(data1, data2): 
            Converts raw data into a list of MeanMaintenanceClassroom objects, associating maintenance types with classrooms.

Dependencies:
    - Pydantic for data validation and serialization.
    - MeanMaintenanceModel and MeanMaintenanceTable for data representation.
    - UUID for handling unique identifiers.
"""

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
    
 
