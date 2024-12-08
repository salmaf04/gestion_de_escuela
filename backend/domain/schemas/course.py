from pydantic import BaseModel

class Course(BaseModel) :
    start_year: int
    end_year: int