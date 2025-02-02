from pydantic import BaseModel, field_validator
import uuid
from enum import Enum
from fastapi import HTTPException, status

class ValidStates(str, Enum) :
    GOOD = "good"
    REGULAR = "regular"
    BAD = "bad"

    @classmethod
    def get_valid_states(cls) :
        return [state.value for state in ValidStates]
    
    @classmethod
    def get_valid_states_str(cls) :
        valid_states_list = cls.get_valid_states()
        return ', '.join(valid_states_list)
    

class ValidType(str, Enum) :
    TECHNOLOGICAL = "technological_mean"
    TEACHING_MATERIAL = "teaching_material"
    OTHER = "other"

    @classmethod
    def get_valid_type(cls) :
        return [state.value for state in ValidType]
    
    @classmethod
    def get_valid_type_str(cls) :
        valid_types_list = cls.get_valid_type()
        return ', '.join(valid_types_list)

class MeanModel (BaseModel):
    id: uuid.UUID
    name: str
    state: str
    location: str
    classroom_id: uuid.UUID
    type: str
    
class MeanCreateModel(BaseModel):
    name: str
    state: str
    location: str 
    classroom_id: uuid.UUID
    type: str

    @field_validator('state')
    def valid_state(cls, state: str) :
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
        lower_state = type.lower()

        if lower_state not in ValidType.get_valid_type() :
            valid_type_str = ValidType.get_valid_type_str()
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Debe insertar un tipo valido : {valid_type_str} "
            )
        return type

class MeanClassroomModel (BaseModel):
    id: uuid.UUID
    name: str
    state: str
    location: str
    type: str
    