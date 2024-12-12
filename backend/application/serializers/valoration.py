from backend.domain.schemas.valoration import ValorationModel
from backend.domain.models.tables import TeacherNoteTable


class ValorationMapper :

    def to_api(self, valoration: TeacherNoteTable) -> ValorationModel :
        return ValorationModel(
            id = valoration.entity_id,
            teacher_id = valoration.teacher_id,
            student_id = valoration.student_id,
            subject_id = valoration.subject_id,
            course_id = valoration.course_id,
            grade = valoration.grade
        )