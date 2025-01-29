from sqlalchemy.orm import Session
from sqlalchemy import select, func
from backend.domain.schemas.absence import AbsenceCreateModel
from backend.domain.models.tables import AbsenceTable, StudentTable, SubjectTable, TeacherTable, CourseTable, teacher_subject_table
from backend.application.services.student import StudentPaginationService
from backend.application.services.course import CoursePaginationService
from backend.application.services.subject import SubjectPaginationService
from backend.domain.filters.absence import AbsenceFilterSchema, AbsenceFilterSet
from datetime import datetime
import uuid
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
    
    def get_absence_by_student(self, session: Session, student_id: uuid.UUID) -> list[AbsenceTable] :
        query = select(AbsenceTable.subject_id , func.count().label("absences_by_subject"))
        query = query.where(AbsenceTable.student_id == student_id)
        query = query.group_by(AbsenceTable.subject_id)
        query = query.subquery()

        final_query = select(query.c.subject_id,query.c.absences_by_subject,SubjectTable, AbsenceTable)
        final_query = final_query.join(query, query.c.subject_id == AbsenceTable.subject_id)
        final_query = final_query.join(SubjectTable, SubjectTable.entity_id == query.c.subject_id)
        final_query = final_query.distinct(SubjectTable.entity_id)
        return session.execute(final_query).all()
    
    def get_absence_by_student_by_teacher(self, session: Session, teacher_id: uuid.UUID) -> list[AbsenceTable] :
        students = self.get_students_by_teacher(session=session, teacher_id=teacher_id)

        query = select(AbsenceTable.student_id, AbsenceTable.subject_id , func.count().label("absences_by_subject"))
        query = query.where( AbsenceTable.student_id.in_(students))
        query = query.group_by(AbsenceTable.subject_id, AbsenceTable.student_id)
        query = query.subquery()
        
        final_query = select(query.c.subject_id, query.c.absences_by_subject, SubjectTable, StudentTable, AbsenceTable, query.c.student_id)
        final_query = final_query.join(query, query.c.subject_id == AbsenceTable.subject_id)
        final_query = final_query.join(StudentTable, StudentTable.entity_id == query.c.student_id)
        final_query = final_query.join(SubjectTable, SubjectTable.entity_id == query.c.subject_id)
        final_query = final_query.distinct(SubjectTable.entity_id, StudentTable.entity_id)
        return session.execute(final_query).all()


    def get_students_by_teacher(self, session: Session, teacher_id: uuid.UUID) -> list[StudentTable] :
        query = (
        select(StudentTable.id)
        .join(CourseTable, StudentTable.course_id == CourseTable.entity_id)
        .join(SubjectTable, CourseTable.entity_id == SubjectTable.course_id)
        .join(teacher_subject_table, SubjectTable.entity_id == teacher_subject_table.c.subject_id)
        .join(TeacherTable, teacher_subject_table.c.teacher_id == TeacherTable.id)
        .where(TeacherTable.id == teacher_id)
        .distinct()
        .subquery()
    )

        return query