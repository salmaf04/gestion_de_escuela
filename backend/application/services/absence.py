from sqlalchemy.orm import Session
from sqlalchemy import select
from backend.domain.schemas.absence import AbsenceCreateModel
from backend.domain.models.tables import AbsenceTable, StudentTable
from backend.application.services.student import StudentPaginationService
from backend.application.services.course import CoursePaginationService
from backend.application.services.subject import SubjectPaginationService
from backend.domain.filters.absence import AbsenceFilterSchema, AbsenceFilterSet
from datetime import datetime

class AbsenceCreateService :

    def create_absence(self, session: Session, absence:AbsenceCreateModel) -> AbsenceTable :
        absence_dict = absence.model_dump(exclude={'date'})
        date = datetime.strptime(absence.date, "%d-%m-%Y")
        new_absence = AbsenceTable(**absence_dict, date=date)

        session.add(new_absence)
        session.commit()
        return new_absence
    
    
class AbsencePaginationService :
    def get_absence(self, session: Session, filter_params: AbsenceFilterSchema) -> list[AbsenceTable] :
        query = select(AbsenceTable)
        filter_set = AbsenceFilterSet(session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return session.execute(query).scalars().all()
    
    
