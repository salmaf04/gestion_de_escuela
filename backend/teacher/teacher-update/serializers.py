from teacher.teacher_common.schemas import TeacherModel
from database.tables import TeacherTable

class TeacherMapper:

    def to_api(self, teacher: TeacherTable) -> TeacherModel:
        return TeacherModel(
            id=teacher.entity_id,
            name=teacher.name,
            fullname=teacher.fullname,
            email=teacher.email,
            specialty=teacher.specialty,
            contract_type=teacher.contract_type,
            experience=teacher.experience
        )