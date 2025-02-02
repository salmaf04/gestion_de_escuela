from pydantic import BaseModel
import uuid
from backend.domain.schemas.mean import MeanClassroomModel

class ClassroomCreateModel(BaseModel):
    number : int
    location : str
    capacity : int

class ClassroomModel(ClassroomCreateModel):
    id: uuid.UUID
    means : list[MeanClassroomModel] | None = None

class ClassroomModelPost(ClassroomCreateModel) :
    id: uuid.UUID
    