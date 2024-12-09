from pydantic import BaseModel
from sqlalchemy_filterset import FilterSet, Filter
from backend.domain.models.tables import AbsenceTable
import uuid


class AbsenceFilterSet(FilterSet):
    student_id = Filter(AbsenceTable.student_id)
    subject_id = Filter(AbsenceTable.subject_id)
    course_id = Filter(AbsenceTable.course_id)
    absences = Filter(AbsenceTable.absences)

class AbsenceFilterSchema(BaseModel):
    student_id : uuid.UUID | None = None
    subject_id : uuid.UUID | None = None
    course_id : uuid.UUID | None = None
    absences : int | None = None