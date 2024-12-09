from pydantic import BaseModel
from sqlalchemy_filterset import FilterSet, Filter
from backend.domain.models.tables import TeacherNoteTable
import uuid


class ValorationFilterSet(FilterSet):
    student_id = Filter(TeacherNoteTable.student_id)
    subject_id = Filter(TeacherNoteTable.subject_id)
    teacher_id = Filter(TeacherNoteTable.teacher_id)
    course_id = Filter(TeacherNoteTable.course_id)
    grade = Filter(TeacherNoteTable.grade)

class ValorationFilterSchema(BaseModel):
    student_id : uuid.UUID | None = None
    subject_id : uuid.UUID | None = None
    teacher_id : uuid.UUID | None = None
    course_id : uuid.UUID | None = None
    grade : int | None = None