from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BooleanFilter
from pydantic import BaseModel
from backend.domain.models.tables import StudentTable
from typing import Optional
import uuid

"""
This module defines filter sets and schemas for managing students using SQLAlchemy and Pydantic.

Classes:
- StudentFilterSet: A filter set for querying students based on name, age, email, and participation in extra activities.
- StudentFilterSchema: A Pydantic model for defining the schema of student filters, allowing optional filtering by name, age range, email, and extra activities participation.
- StudentChangeRequest: A Pydantic model for defining the schema of change requests for students, allowing optional updates to various attributes.

Dependencies:
- SQLAlchemy's FilterSet, Filter, RangeFilter, and BooleanFilter for creating query filters.
- Pydantic's BaseModel for defining data validation and serialization.
- Optional from typing for optional fields.

Attributes:
- name (str | None): The name of the student to filter by or update.
- age (tuple[int, int] | int | None): The age range to filter by or the age to update.
- email (str | None): The email of the student to filter by or update.
- extra_activities (bool | None): The participation in extra activities to filter by or update.
- username (str | None): The username for updating a student's credentials.
- hash_password (str | None): The hashed password for updating a student's credentials.
"""

class StudentFilterSet(FilterSet):
    id = Filter(StudentTable.id)
    name = Filter(StudentTable.name)
    age = RangeFilter(StudentTable.age)
    email = Filter(StudentTable.email)
    extra_activities = BooleanFilter(StudentTable.extra_activities)

class StudentFilterSchema(BaseModel):
    name : str | None = None
    id : uuid.UUID | None = None
    age : tuple[int, int] | None = None
    email : str | None = None
    extra_activities : bool | None = None

class StudentChangeRequest(BaseModel) :
    name : Optional[str] = None
    lastname : Optional[str] = None
    age : Optional[int] = None
    email : Optional[str] = None
    extra_activities : Optional[bool] = None
    username : Optional[str] = None
    hash_password : Optional[str] = None
    course_id : Optional[uuid.UUID] = None