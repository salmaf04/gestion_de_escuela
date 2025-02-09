from pydantic import BaseModel

"""
This module defines a Pydantic model for managing change requests related to valoration periods.

Classes:
- ValorationPeriodChangeRequest: A Pydantic model for defining the schema of change requests for valoration periods, allowing optional updates to the open status.

Dependencies:
- Pydantic's BaseModel for defining data validation and serialization.

Attributes:
- open (bool | None): The open status of the valoration period, indicating whether the period is open or closed. This attribute is optional.
"""

class ValorationPeriodChangeRequest(BaseModel):
    open : bool | None = None

class ValorationPeriodModel(BaseModel):
    open : bool