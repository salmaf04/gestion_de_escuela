from pydantic import BaseModel
from sqlalchemy_filterset import FilterSet, Filter
from backend.domain.models.tables import AbsenceTable
import uuid


class AbsenceFilterSet(FilterSet):
    student_id = Filter(AbsenceTable.student_id)
    subject_id = Filter(AbsenceTable.subject_id)
    date = Filter(AbsenceTable.date)

class AbsenceFilterSchema(BaseModel):
    student_id : uuid.UUID | None = None
    subject_id : uuid.UUID | None = None
    date : str | None = None