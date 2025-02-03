from pydantic import BaseModel

"""
This module defines base classes for Pydantic models used in the application.

Classes:
    BaseEntity: A base class for Pydantic models representing entities in the application.
    BaseCreateModel: A base class for Pydantic models used for creating new entities.

Class Details:

1. BaseEntity:
    - Inherits from Pydantic's BaseModel.
    - Serves as a base class for defining entity models in the application.
    - Can be extended to include common attributes or methods shared across entity models.

2. BaseCreateModel:
    - Inherits from Pydantic's BaseModel.
    - Serves as a base class for defining models used for creating new entities.
    - Can be extended to include common attributes or methods shared across creation models.

Dependencies:
    - Pydantic for data validation and serialization.
"""

class BaseEntity(BaseModel):
    pass 

class BaseCreateModel(BaseModel):
    pass