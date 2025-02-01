from sqlalchemy.orm import Session
from sqlalchemy import select, func
from backend.domain.schemas.absence import AbsenceCreateModel
from backend.domain.models.tables import AbsenceTable, StudentTable, SubjectTable, TeacherTable, CourseTable, teacher_subject_table
from backend.application.services.student import StudentPaginationService
from backend.application.services.course import CoursePaginationService
from backend.application.services.subject import SubjectPaginationService
from backend.domain.filters.absence import AbsenceFilterSchema, AbsenceFilterSet
from datetime import datetime
from .. import IRepository
import uuid

class AbsenceRepository(IRepository[AbsenceCreateModel,AbsenceTable, None,AbsenceFilterSchema]):
    def __init__(self, session):
        super().__init__(session)

    def create(self, entity: AbsenceCreateModel) -> AbsenceTable :
        absence_dict = entity.model_dump(exclude={'date'})
        date = datetime.strptime(entity.date, "%d-%m-%Y")
        new_absence = AbsenceTable(**absence_dict, date=date)

        self.session.add(new_absence)
        self.session.commit()
        return new_absence
    
    def get(self, filter_params: AbsenceFilterSchema) -> list[AbsenceTable] :
        query = select(AbsenceTable)
        filter_set = AbsenceFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return self.session.execute(query).scalars().all()
    
    def get_by_id(self, id: str) -> AbsenceTable :
        pass

    def delete(self, entity: AbsenceTable) -> None :
        pass

    def update(self, changes : None , entity : AbsenceTable) -> AbsenceTable:
        pass
        
    def get_absence_by_student(self, student_id: uuid.UUID) -> list[AbsenceTable] :
        query = select(AbsenceTable.subject_id , func.count().label("absences_by_subject"))
        query = query.where(AbsenceTable.student_id == student_id)
        query = query.group_by(AbsenceTable.subject_id)
        query = query.subquery()

        final_query = select(query.c.subject_id,query.c.absences_by_subject,SubjectTable, AbsenceTable)
        final_query = final_query.join(query, query.c.subject_id == AbsenceTable.subject_id)
        final_query = final_query.join(SubjectTable, SubjectTable.entity_id == query.c.subject_id)
        final_query = final_query.distinct(SubjectTable.entity_id)
        return self.session.execute(final_query).all()
    
    def get_absence_by_student_by_teacher(self, teacher_id: uuid.UUID) -> list[AbsenceTable] :
        students = self.get_students_by_teacher(session=self.session, teacher_id=teacher_id)

        query = select(AbsenceTable.student_id, AbsenceTable.subject_id , func.count().label("absences_by_subject"))
        query = query.where( AbsenceTable.student_id.in_(students))
        query = query.group_by(AbsenceTable.subject_id, AbsenceTable.student_id)
        query = query.subquery()
        
        final_query = select(query.c.subject_id, query.c.absences_by_subject, SubjectTable, StudentTable, AbsenceTable, query.c.student_id)
        final_query = final_query.join(query, query.c.subject_id == AbsenceTable.subject_id)
        final_query = final_query.join(StudentTable, StudentTable.entity_id == query.c.student_id)
        final_query = final_query.join(SubjectTable, SubjectTable.entity_id == query.c.subject_id)
        final_query = final_query.distinct(SubjectTable.entity_id, StudentTable.entity_id)
        return self.session.execute(final_query).all()


    def get_students_by_teacher(self, teacher_id: uuid.UUID) -> list[StudentTable] :
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