from backend.domain.schemas.teacher import TeacherModel
from backend.domain.models.tables import TeacherTable

class TeacherMapper :

    def to_api(self, teacher: TeacherTable , subjects: list[str]) -> TeacherModel :
        return TeacherModel(
            id = teacher.entity_id,
            name=teacher.name,
            fullname=teacher.fullname,
            email=teacher.email,
            specialty=teacher.specialty,
            contract_type=teacher.contract_type,
            experience=teacher.experience,
            username=teacher.username,
            list_of_subjects=subjects
        )