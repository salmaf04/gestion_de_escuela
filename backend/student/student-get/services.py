from sqlalchemy.orm import Session
from database.tables import StudentTable
from sqlalchemy import select
from .filters import StudentFilterSet , StudentFilterSchema


class StudentListingService:
    def get_students(self, session: Session, filter_params: StudentFilterSchema) -> list[StudentTable] :
        query = select(StudentTable)
        filter_set = StudentFilterSet(session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return session.execute(query).scalars().all()