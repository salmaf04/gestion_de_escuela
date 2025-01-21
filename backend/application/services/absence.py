from sqlalchemy.orm import Session
from sqlalchemy import select
from backend.domain.schemas.absence import AbsenceCreateModel
from backend.domain.models.tables import AbsenceTable
from backend.application.services.student import StudentPaginationService
from backend.application.services.course import CoursePaginationService
from backend.application.services.subject import SubjectPaginationService
from backend.domain.filters.absence import AbsenceFilterSchema, AbsenceFilterSet



class AbsenceCreateService :

    def create_absence(self, session: Session, absence:AbsenceCreateModel) -> AbsenceTable :
        absence_dict = absence.model_dump()
        new_absence = AbsenceTable(**absence_dict)

        student = StudentPaginationService().get_student_by_id(session=session, id=absence.student_id)
        course = CoursePaginationService().get_course_by_id(session=session, id=absence.course_id)
        subject = SubjectPaginationService().get_subject_by_id(session=session, id=absence.subject_id)

        new_absence.student = student
        new_absence.course = course   
        new_absence.subject = subject

        student.student_absence_association.append(new_absence)
        course.student_absence_association.append(new_absence)
        subject.student_absence_association.append(new_absence)

        session.add(new_absence)
        session.commit()
        return new_absence
    
    
class AbsencePaginationService :
    def get_absence(self, session: Session, filter_params: AbsenceFilterSchema) -> list[AbsenceTable] :
        query = select(AbsenceTable)
        filter_set = AbsenceFilterSet(session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return session.execute(query).scalars().all()
    
