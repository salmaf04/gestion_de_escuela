from pydantic import BaseModel

class Course(BaseModel) :
    course: tuple[int, int]