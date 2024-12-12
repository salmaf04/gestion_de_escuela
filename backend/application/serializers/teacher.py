from backend.domain.schemas.teacher import TeacherModel
from backend.domain.models.tables import TeacherTable

class TeacherMapper :

    def to_api(self, teacher: TeacherTable , subjects: list[str] , valoration: float = None) -> TeacherModel :
        return TeacherModel(
            id = teacher.entity_id,
            name=teacher.name,
            fullname=teacher.fullname,
            email=teacher.email,
            specialty=teacher.specialty,
            contract_type=teacher.contract_type,
            experience=teacher.experience,
            username=teacher.username,
            list_of_subjects=subjects,
            valoration=valoration if valoration else "No hay valoraciones"
        )
    
    def to_subject_list(self, subjects) :
        names = []
        for subject in subjects :
            names.append(subject.name)
        return names