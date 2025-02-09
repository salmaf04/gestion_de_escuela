from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BooleanFilter
from pydantic import BaseModel
from backend.domain.models.tables import StudentNoteTable
import uuid
from typing import Optional

"""
This module defines filter sets and schemas for managing student notes using SQLAlchemy and Pydantic.

Classes:
- NoteFilterSet: A filter set for querying student notes based on student ID, subject ID, teacher ID, and note value.
- NoteFilterSchema: A Pydantic model for defining the schema of note filters, allowing optional filtering by student ID, subject ID, teacher ID, and note value.
- NoteChangeRequest: A Pydantic model for defining the schema of change requests for student notes, allowing optional updates to the note value.

Dependencies:
- SQLAlchemy's FilterSet and Filter for creating query filters.
- Pydantic's BaseModel for defining data validation and serialization.
- UUID for handling unique identifiers.
- Optional from typing for optional fields.

Attributes:
- student_id (uuid.UUID | None): The ID of the student to filter notes by.
- subject_id (uuid.UUID | None): The ID of the subject to filter notes by.
- teacher_id (uuid.UUID | None): The ID of the teacher to filter notes by.
- note_value (int | None): The value of the note to filter by or update.
"""

class NoteFilterSet(FilterSet):
    id = Filter(StudentNoteTable.entity_id)
    student_id = Filter(StudentNoteTable.student_id)
    subject_id = Filter(StudentNoteTable.subject_id)
    teacher_id = Filter(StudentNoteTable.teacher_id)
    note_value = Filter(StudentNoteTable.note_value)

class NoteFilterSchema(BaseModel):
    id : uuid.UUID | None = None
    student_id : uuid.UUID | None = None
    subject_id : uuid.UUID | None = None
    teacher_id : uuid.UUID | None = None
    note_value : int | None = None

class NoteChangeRequest(BaseModel) :
    note_value : Optional[int] = None