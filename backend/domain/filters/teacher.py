from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BooleanFilter, BaseFilter
from pydantic import BaseModel, Field
from backend.domain.models.tables import TeacherTable
from typing import Optional
import uuid
from sqlalchemy import Select
from sqlalchemy.orm import Session
from typing import Any

"""
This module defines filter sets and schemas for managing teachers using SQLAlchemy and Pydantic.

Classes:
- TeacherAlertFilter: A custom filter for querying teachers with alerts based on their valoration.
- TeacherFilterSet: A filter set for querying teachers based on ID, name, email, specialty, contract type, experience, and alert status.
- TeacherFilterSchema: A Pydantic model for defining the schema of teacher filters, allowing optional filtering by various attributes.
- TeacherChangeRequest: A Pydantic model for defining the schema of change requests for teachers, allowing optional updates to various attributes.

Dependencies:
- SQLAlchemy's FilterSet, Filter, and RangeFilter for creating query filters.
- Pydantic's BaseModel for defining data validation and serialization.
- Optional from typing for optional fields.
- UUID for handling unique identifiers.

Attributes:
- id (uuid.UUID | None): The ID of the teacher to filter by.
- name (str | None): The name of the teacher to filter by or update.
- email (str | None): The email of the teacher to filter by.
- specialty (str | None): The specialty of the teacher to filter by or update.
- contract_type (str | None): The contract type of the teacher to filter by or update.
- experience (tuple[int, int] | int | None): The experience range to filter by or the experience to update.
- alert (bool | None): The alert status to filter by.
- full_name (str | None): The full name of the teacher to update.
"""

class TeacherAlertFilter(BaseFilter) :
    def filter(self, query: Select, value: bool, values: Any) :
        teacher_table = TeacherTable
        return query.where(
            teacher_table.less_than_three_valoration >= 5
        )
        

class TeacherFilterSet(FilterSet):
    id = Filter(TeacherTable.id)
    name = Filter(TeacherTable.name)
    email = Filter(TeacherTable.email)
    specialty = Filter(TeacherTable.specialty)
    contract_type = Filter(TeacherTable.contract_type)
    experience = RangeFilter(TeacherTable.experience)
    alert = TeacherAlertFilter()

class TeacherFilterSchema(BaseModel):
    id : uuid.UUID | None = None
    name : str | None = None
    email : str | None = None
    specialty : str | None = None
    contract_type : str | None = None
    experince : tuple[int, int] | None = None
    alert : bool | None = None
    
class TeacherChangeRequest(BaseModel) :
    name : Optional[str] = None
    lastname : Optional[str] = None
    full_name : Optional[str] = None
    specialty : Optional[str] = None
    contract_type : Optional[str] = None
    experience : Optional[int] = None
   