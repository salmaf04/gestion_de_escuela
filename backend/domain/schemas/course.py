from pydantic import BaseModel

class Course(BaseModel) :
    id : int
    start_year: int
    end_year: int