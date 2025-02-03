from pydantic import BaseModel
import uuid

"""
This module defines Pydantic models for representing mean request and deletion data in the application.

Classes:
    MeanRequestCreateModel: A model for creating new mean request records.
    MeanRequestModel: A model representing a mean request with detailed attributes.
    MeanDeletionModel: A model for representing mean deletion requests.

Class Details:

1. MeanRequestCreateModel:
    - Inherits from Pydantic's BaseModel.
    - Represents the data required to create a new mean request.
    - Attributes:
        - mean_id: The unique identifier of the mean (UUID).

2. MeanRequestModel:
    - Inherits from Pydantic's BaseModel.
    - Represents a mean request with detailed attributes.
    - Attributes:
        - teacher_id: The unique identifier of the teacher making the request (UUID).
        - mean_id: The unique identifier of the mean (UUID).

3. MeanDeletionModel:
    - Inherits from Pydantic's BaseModel.
    - Represents a request to delete a mean.
    - Attributes:
        - mean_id: The unique identifier of the mean to be deleted (UUID).

Dependencies:
    - Pydantic for data validation and serialization.
    - UUID for handling unique identifiers.
"""
class MeanRequestCreateModel(BaseModel) :
    mean_id : uuid.UUID


class MeanRequestModel(BaseModel) :
    teacher_id : uuid.UUID
    mean_id : uuid.UUID

class MeanDeletionModel(BaseModel) :
     mean_id : uuid.UUID
