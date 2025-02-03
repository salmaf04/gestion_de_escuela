from pydantic import BaseModel
import uuid


class MeanRequestCreateModel(BaseModel) :
    mean_id : uuid.UUID


class MeanRequestModel(BaseModel) :
    teacher_id : uuid.UUID
    mean_id : uuid.UUID

class MeanDeletionModel(BaseModel) :
     mean_id : uuid.UUID
