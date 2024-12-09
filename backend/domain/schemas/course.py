from pydantic import BaseModel
import uuid

class CourseCreateModel(BaseModel) :
    start_year: int
    end_year: int

class CourseModel(CourseCreateModel) :
    id : uuid.UUID
