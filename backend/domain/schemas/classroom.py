from pydantic import BaseModel
import uuid
from backend.domain.schemas.mean import MeanClassroomModel

class ClassroomCreateModel(BaseModel):
    location : str
    capacity : int

class ClassroomModel(ClassroomCreateModel):
    id: uuid.UUID
    means : list[MeanClassroomModel]

class ClassroomModelPost(ClassroomCreateModel) :
    id: uuid.UUID
    