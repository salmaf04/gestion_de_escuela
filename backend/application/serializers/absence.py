from backend.domain.schemas.absence import AbsenceModel
from backend.domain.models.tables import AbsenceTable

class AbsenceMapper :

    def to_api(self, absence: AbsenceTable) -> AbsenceModel :
        return AbsenceModel(
            id = absence.entity_id,
            student_id = absence.student_id,
            course_id = absence.course_id,
            subject_id = absence.subject_id,
            absences = absence.absences
        )