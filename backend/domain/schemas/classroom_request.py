from pydantic import BaseModel
import uuid


class ClassroomRequestCreateModel(BaseModel) :
    classroom_id : uuid.UUID


class ClassroomRequestModel(BaseModel) :
    teacher_id : uuid.UUID
    classroom_id : uuid.UUID

class ClassroomDeletionModel(BaseModel) :
     classroom_id : uuid.UUID