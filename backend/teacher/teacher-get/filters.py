from sqlalchemy_filterset import FilterSet, Filter, RangeFilter, BooleanFilter
from pydantic import BaseModel
from database.tables import TeacherTable


class TeacherFilterSet(FilterSet):
    email = Filter(TeacherTable.email)
    specialty = Filter(TeacherTable.specialty)
    contract_type = Filter(TeacherTable.contract_type)
    experience = RangeFilter(TeacherTable.experience)

class TeacherFilterSchema(BaseModel):
    email : str | None = None
    specialty : str | None = None
    contract_type : str | None = None
    experince : tuple[int, int] | None = None