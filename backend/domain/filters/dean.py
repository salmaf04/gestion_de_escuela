from sqlalchemy_filterset import FilterSet, Filter, RangeFilter
from pydantic import BaseModel
from backend.domain.models.tables import DeanTable
from typing import Optional

"""
This module defines filter sets and schemas for managing deans using SQLAlchemy and Pydantic.

Classes:
- DeanFilterSet: A filter set for querying deans based on name, email, specialty, contract type, and experience.
- DeanFilterSchema: A Pydantic model for defining the schema of dean filters, allowing optional filtering by name, email, specialty, contract type, and experience range.
- DeanChangeRequest: A Pydantic model for defining the schema of change requests for deans, allowing optional updates to various attributes.

Dependencies:
- SQLAlchemy's FilterSet, Filter, and RangeFilter for creating query filters.
- Pydantic's BaseModel for defining data validation and serialization.
- Optional from typing for optional fields.

Attributes:
- name (str | None): The name of the dean to filter by or update.
- email (str | None): The email of the dean to filter by or update.
- specialty (str | None): The specialty of the dean to filter by or update.
- contract_type (str | None): The contract type of the dean to filter by or update.
- experience (tuple[int, int] | int | None): The experience range to filter by or the experience to update.
- full_name (str | None): The full name of the dean to update.
- username (str | None): The username for updating a dean's credentials.
- hash_password (str | None): The hashed password for updating a dean's credentials.
"""

class DeanFilterSet(FilterSet):
    name = Filter(DeanTable.name)
    email = Filter(DeanTable.email)
    specialty = Filter(DeanTable.specialty)
    contract_type = Filter(DeanTable.contract_type)
    experience = RangeFilter(DeanTable.experience)

class DeanFilterSchema(BaseModel):
    name : str | None = None
    email : str | None = None
    specialty : str | None = None
    contract_type : str | None = None
    experince : tuple[int, int] | None = None
    
class DeanChangeRequest(BaseModel) :
    name : Optional[str] = None
    lastname : Optional[str] = None
    full_name : Optional[str] = None
    email : Optional[str] = None
    specialty : Optional[str] = None
    contract_type : Optional[str] = None
    experience : Optional[int] = None
    username : Optional[str] = None
    hash_password : Optional[str] = None