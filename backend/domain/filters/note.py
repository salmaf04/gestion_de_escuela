from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BooleanFilter
from pydantic import BaseModel
from backend.domain.models.tables import StudentNoteTable
import uuid
from typing import Optional

class NoteFilterSet(FilterSet):
    student_id = Filter(StudentNoteTable.student_id)
    subject_id = Filter(StudentNoteTable.subject_id)
    teacher_id = Filter(StudentNoteTable.teacher_id)
    note_value = Filter(StudentNoteTable.note_value)

class NoteFilterSchema(BaseModel):
    student_id : uuid.UUID | None = None
    subject_id : uuid.UUID | None = None
    teacher_id : uuid.UUID | None = None
    note_value : int | None = None

class NoteChangeRequest(BaseModel) :
    note_value : Optional[int] = None