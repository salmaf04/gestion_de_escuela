from pydantic import BaseModel
import uuid

class CourseCreateModel(BaseModel) :
    year : int

class CourseModel(CourseCreateModel) :
    id : uuid.UUID
