from backend.domain.schemas.classroom import ClassroomModel, ClassroomModelPost
from backend.domain.schemas.mean import MeanClassroomModel
from backend.domain.models.tables import ClassroomTable

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
            location = classroom.location,
            capacity = classroom.capacity
        )
    

    
                                                                        