from pydantic import BaseModel
from sqlalchemy_filterset import FilterSet, Filter
from backend.domain.models.tables import AbsenceTable
import uuid

"""
This module defines filter sets and schemas for managing absences using SQLAlchemy and Pydantic.

Classes:
- AbsenceFilterSet: A filter set for querying absences based on student ID, subject ID, and date.
- AbsenceFilterSchema: A Pydantic model for defining the schema of absence filters, allowing optional filtering by student ID, subject ID, and date.

Dependencies:
- SQLAlchemy's FilterSet and Filter for creating query filters.
- Pydantic's BaseModel for defining data validation and serialization.
- UUID for handling unique identifiers.

Attributes:
- student_id (uuid.UUID | None): The ID of the student to filter absences by.
- subject_id (uuid.UUID | None): The ID of the subject to filter absences by.
- date (str | None): The date to filter absences by.
"""

class AbsenceFilterSet(FilterSet):
    student_id = Filter(AbsenceTable.student_id)
    subject_id = Filter(AbsenceTable.subject_id)
    date = Filter(AbsenceTable.date)

class AbsenceFilterSchema(BaseModel):
    student_id : uuid.UUID | None = None
    subject_id : uuid.UUID | None = None
    date : str | None = None