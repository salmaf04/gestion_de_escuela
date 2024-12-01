from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BooleanFilter
from pydantic import BaseModel
from database.tables import StudentTable


class StudentFilterSet(FilterSet):
    name = Filter(StudentTable.name)
    age = RangeFilter(StudentTable.age)
    email = Filter(StudentTable.email)
    extra_activities = BooleanFilter(StudentTable.extra_activities)

class StudentFilterSchema(BaseModel):
    name : str | None = None
    age : tuple[int, int] | None = None
    email : str | None = None
    extra_activities : bool | None = None
