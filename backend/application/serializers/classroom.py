from backend.domain.schemas.classroom import ClassroomModel
from backend.domain.models.tables import ClassroomTable

class ClassroomMapper :

    def to_api(self, classroom: ClassroomTable) -> ClassroomModel :
        return ClassroomModel(
            id = classroom.entity_id,
            location = classroom.location,
            capacity = classroom.capacity
        )