from pydantic import BaseModel
from sqlalchemy_filterset import FilterSet, Filter, BaseFilter
from backend.domain.models.tables import TeacherNoteTable, TeacherTable
import uuid
from sqlalchemy import Select
from typing import Any

"""
This module defines filter sets and schemas for managing valorations using SQLAlchemy and Pydantic.

Classes:
- ValorationFilterSet: A filter set for querying valorations based on student ID, subject ID, teacher ID, course ID, and grade.
- ValorationFilterSchema: A Pydantic model for defining the schema of valoration filters, allowing optional filtering by various attributes.

Dependencies:
- SQLAlchemy's FilterSet and Filter for creating query filters.
- Pydantic's BaseModel for defining data validation and serialization.
- UUID for handling unique identifiers.

Attributes:
- student_id (uuid.UUID | None): The ID of the student to filter valorations by.
- subject_id (uuid.UUID | None): The ID of the subject to filter valorations by.
- teacher_id (uuid.UUID | None): The ID of the teacher to filter valorations by.
- course_id (uuid.UUID | None): The ID of the course to filter valorations by.
- grade (int | None): The grade to filter valorations by.
"""

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
   