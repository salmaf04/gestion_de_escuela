from backend.domain.schemas.absence import AbsenceModel
from backend.domain.schemas.student import StudentModel
from backend.domain.models.tables import AbsenceTable
from backend.application.serializers.student import StudentMapper

class AbsenceMapper :

    def to_api(self, absence: AbsenceTable) -> AbsenceModel :
        return AbsenceModel(
            id = absence.entity_id,
            student_id = absence.student_id,
            subject_id = absence.subject_id,
            date = absence.date.strftime("%d-%m-%Y")
        )
    
    def to_abscence_by_student(self, data) :
        serialized_values = []
        absences_total = len(data)

        for absence in data :
            serialized_values.append(
                self.to_api(absence)
            )
        serialized_values.append({"total abscences": absences_total})
        return serialized_values