from backend.domain.schemas.classroom import ClassroomModel, ClassroomModelPost
from backend.domain.schemas.mean import MeanClassroomModel
from backend.domain.models.tables import ClassroomTable

"""
This module defines a mapper for converting classroom data into API representations.

Classes:
    ClassroomMapper: A utility class for mapping classroom data to ClassroomModel and ClassroomModelPost objects.

Class Details:

ClassroomMapper:
    - This class provides methods to convert classroom data, including associated means, into API models used in the application layer.
    
    Methods:
        - to_api(data) -> list[ClassroomModel]: 
            Converts a list of classroom data into a list of ClassroomModel objects. It handles the association of means with classrooms and ensures that each classroom is represented only once, with all its associated means.
        - to_api_default(classroom: ClassroomTable) -> ClassroomModelPost: 
            Converts a ClassroomTable object into a ClassroomModelPost object, mapping the basic fields without associated means.

Dependencies:
    - ClassroomModel, ClassroomModelPost, and MeanClassroomModel for data representation.
    - ClassroomTable for database representation.
"""


class ClassroomMapper :


    def to_api(self, data) -> ClassroomModel :
        serialized_values = []
        ids = []

        for classroom in data :
            if classroom[0].entity_id in ids :
                serialized_values[len(serialized_values)-1].means.append(
                    MeanClassroomModel(
                        id = classroom[1].id,
                        name = classroom[1].name,
                        state = classroom[1].state,
                        location = classroom[1].location,
                        type = classroom[1].type
                    )
                )
            else :
                ids.append(classroom[0].entity_id)
                
                new_classroom = ClassroomModel(
                    id = classroom[0].entity_id,
                    number= classroom[0].number,
                    location = classroom[0].location,
                    capacity = classroom[0].capacity,
                    means = [
                        MeanClassroomModel(
                            id = classroom[1].id,
                            name = classroom[1].name,
                            state = classroom[1].state,
                            location = classroom[1].location,
                            type = classroom[1].type
                        )
                    ] if classroom[1] else None
                )
                serialized_values.append(new_classroom)

        return serialized_values

    def to_api_default(self, classroom: ClassroomTable) -> ClassroomModelPost :
        return  ClassroomModelPost(
            id = classroom.entity_id,
            number = classroom.number,
            location = classroom.location,
            capacity = classroom.capacity
        )
    

    
                                                                        