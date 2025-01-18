from backend.domain.schemas.classroom_request import ClassroomRequestModel


class ClassroomRequestMapper :
    def to_api(self,teacher_id, classroom_id) :
        return ClassroomRequestModel(
            teacher_id=teacher_id,
            classroom_id=classroom_id
        )
