from backend.domain.schemas.absence import AbsenceModel
from backend.domain.schemas.student import StudentModel
from backend.domain.models.tables import AbsenceTable
from backend.application.serializers.student import StudentMapper
from backend.application.serializers.subject import SubjectMapper
from pydantic import BaseModel
import uuid

class PruebaMapper(BaseModel) :
    id : uuid.UUID
    count : int


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
      
        for absence in data :
            serialized_values.append(
                self.to_api(absence[2])
            )

        absences_by_subject = self.calculate_absence_by_subject(data)   
    
        return serialized_values , absences_by_subject
    
    def calculate_absence_by_subject(self, data) :
        absences_by_subject = {}

        for absence in data :
            if absence[0] not in absences_by_subject :
                absences_by_subject.update({f"Total de ausencias en {absence[3].name}" : absence[1]})

        return absences_by_subject