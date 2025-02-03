from pydantic import BaseModel
import uuid

"""
This module defines Pydantic models for representing course data in the application.

Classes:
    CourseCreateModel: A model for creating new course records.
    CourseModel: A model representing a course with additional attributes.

Class Details:

1. CourseCreateModel:
    - Inherits from Pydantic's BaseModel.
    - Represents the data required to create a new course.
    - Attributes:
        - year: The year associated with the course (integer).

2. CourseModel:
    - Inherits from CourseCreateModel.
    - Represents a course with additional attributes.
    - Attributes:
        - id: The unique identifier of the course (UUID).

Dependencies:
    - Pydantic for data validation and serialization.
    - UUID for handling unique identifiers.
"""

class CourseCreateModel(BaseModel) :
    year : int

class CourseModel(CourseCreateModel) :
    id : uuid.UUID
