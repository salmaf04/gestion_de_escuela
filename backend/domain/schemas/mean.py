"""
Pydantic models and enums for resource/mean data validation and serialization.
These models define the structure and validation rules for resources in the system.
"""

from pydantic import BaseModel, field_validator
import uuid
from enum import Enum
from fastapi import HTTPException, status

class ValidStates(str, Enum) :
    """
    Enumeration of valid states for resources.
    Defines possible conditions a resource can be in.
    Attributes:
        - GOOD: Resource is in good condition
        - REGULAR: Resource is in regular condition
        - BAD: Resource needs attention
    """
    GOOD = "good"
    REGULAR = "regular"
    BAD = "bad"

    @classmethod
    def get_valid_states(cls) :
        """Returns a list of all valid state values."""
        return [state.value for state in ValidStates]
    
    @classmethod
    def get_valid_states_str(cls) :
        """Returns a comma-separated string of all valid states for error messages."""
        valid_states_list = cls.get_valid_states()
        return ', '.join(valid_states_list)
    

class ValidType(str, Enum) :
    """
    Enumeration of valid resource types.
    Defines the categories of resources that can exist in the system.
    Attributes:
        - TECHNOLOGICAL: Electronic or technological equipment
        - TEACHING_MATERIAL: Educational materials
        - OTHER: Miscellaneous resources
    """
    TECHNOLOGICAL = "technological_mean"
    TEACHING_MATERIAL = "teaching_material"
    OTHER = "other"

    @classmethod
    def get_valid_type(cls) :
        """Returns a list of all valid type values."""
        return [state.value for state in ValidType]
    
    @classmethod
    def get_valid_type_str(cls) :
        """Returns a comma-separated string of all valid types for error messages."""
        valid_types_list = cls.get_valid_type()
        return ', '.join(valid_types_list)

class MeanModel (BaseModel):
    """
    Pydantic model for representing a complete resource record.
    Used for responses and data serialization.
    Attributes:
        - id: UUID identifier for the resource
        - name: Resource name
        - state: Current condition of the resource
        - location: Physical location
        - classroom_id: Associated classroom (optional)
        - to_be_replaced: Flag indicating if replacement is needed
        - type: Resource category
    """
    id: uuid.UUID
    name: str
    state: str
    location: str
    classroom_id: uuid.UUID | None
    to_be_replaced: bool | None = None
    requested_by: str | None = None
    type: str
    
class MeanCreateModel(BaseModel):
    """
    Pydantic model for creating a new resource.
    Includes validation for state and type fields.
    Attributes:
        - name: Resource name
        - state: Current condition (must be valid state)
        - location: Physical location
        - classroom_id: Associated classroom
        - type: Resource category (must be valid type)
    """
    name: str
    state: str
    location: str 
    classroom_id: uuid.UUID
    type: str

    @field_validator('state')
    def valid_state(cls, state: str) :
        """
        Validates that the state value is one of the allowed states.
        Raises HTTP 422 error if state is invalid.
        """
        lower_state = state.lower()

        if lower_state not in ValidStates.get_valid_states() :
            valid_states_str = ValidStates.get_valid_states_str()
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Debe insertar un estado valido : {valid_states_str} "
            )
        return state
    
    @field_validator('type')
    def valid_type(cls, type: str) :
        """
        Validates that the type value is one of the allowed types.
        Raises HTTP 422 error if type is invalid.
        """
        lower_state = type.lower()

        if lower_state not in ValidType.get_valid_type() :
            valid_type_str = ValidType.get_valid_type_str()
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Debe insertar un tipo valido : {valid_type_str} "
            )
        return type

class MeanClassroomModel (BaseModel):
    """
    Pydantic model for representing a resource in classroom context.
    Simplified version of MeanModel without classroom-specific fields.
    Attributes:
        - id: UUID identifier for the resource
        - name: Resource name
        - state: Current condition
        - location: Physical location
        - type: Resource category
    """
    id: uuid.UUID
    name: str
    state: str
    location: str
    type: str
    