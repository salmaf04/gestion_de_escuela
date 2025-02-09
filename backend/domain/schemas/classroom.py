from pydantic import BaseModel
import uuid
from backend.domain.schemas.mean import MeanClassroomModel

"""
This module defines Pydantic models for representing classroom data in the application.

Classes:
    ClassroomCreateModel: A model for creating new classroom records.
    ClassroomModel: A model representing a classroom with additional attributes.
    ClassroomModelPost: A model for posting classroom data with an ID.

Class Details:

1. ClassroomCreateModel:
    - Inherits from Pydantic's BaseModel.
    - Represents the data required to create a new classroom.
    - Attributes:
        - number: The classroom number (integer).
        - location: The location of the classroom (string).
        - capacity: The capacity of the classroom (integer).

2. ClassroomModel:
    - Inherits from ClassroomCreateModel.
    - Represents a classroom with additional attributes.
    - Attributes:
        - id: The unique identifier of the classroom (UUID).
        - means: An optional list of MeanClassroomModel objects representing means associated with the classroom.

3. ClassroomModelPost:
    - Inherits from ClassroomCreateModel.
    - Represents classroom data for posting, including an ID.
    - Attributes:
        - id: The unique identifier of the classroom (UUID).

Dependencies:
    - Pydantic for data validation and serialization.
    - UUID for handling unique identifiers.
    - MeanClassroomModel for representing means associated with classrooms.
"""
class ClassroomCreateModel(BaseModel):
    number : int
    location : str
    capacity : int

class ClassroomModel(ClassroomCreateModel):
    id: uuid.UUID
    requested_by : str | None = None
    means : list[MeanClassroomModel] | None = None

class ClassroomModelPost(ClassroomCreateModel) :
    id: uuid.UUID

    