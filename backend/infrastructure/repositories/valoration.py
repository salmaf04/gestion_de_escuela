from sqlalchemy.orm import Session
from backend.domain.schemas.valoration import ValorationCreateModel
from backend.domain.models.tables import TeacherNoteTable, TeacherTable, StudentTable, SubjectTable, CourseTable
from backend.application.services.student import StudentPaginationService
from backend.application.services.subject import SubjectPaginationService
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.course import CoursePaginationService
from backend.domain.filters.valoration import ValorationFilterSchema, ValorationFilterSet
from sqlalchemy import select, func, update
from .base import IRepository

class ValorationRepository(IRepository[ValorationCreateModel,TeacherNoteTable, None,ValorationFilterSchema]):
    def __init__(self, session):
        super().__init__(session)

    def create(
        self,
        valoration: ValorationCreateModel,
        student : StudentTable,
        subject : SubjectTable,
        teacher : TeacherTable,
        course : CourseTable                       
    ) -> TeacherNoteTable : 
        
        valoration_dict = valoration.model_dump()
        new_valoration = TeacherNoteTable(**valoration_dict)
        
        new_valoration.student = student
        new_valoration.subject = subject  
        new_valoration.teacher = teacher
        new_valoration.course = course

        teacher.teacher_note_association.append(new_valoration)
        subject.teacher_note_association.append(new_valoration)
        student.teacher_note_association.append(new_valoration)
        course.teacher_note_association.append(new_valoration)

        self.session.add(new_valoration)
        self.session.commit()
        return new_valoration

    def delete(self, entity: TeacherNoteTable) -> None :
        pass

    def update(self, changes : None , entity : TeacherNoteTable, modified_by : str) -> TeacherNoteTable :
        pass

    def get_by_id(self, id: str ) -> TeacherNoteTable :
        query = self.session.query(TeacherNoteTable).filter(TeacherNoteTable.entity_id == id)

        result = query.scalar()

        return result

    def get(self, filter_params: ValorationFilterSchema) -> list[TeacherNoteTable] :
        query = select(TeacherNoteTable)
        filter_set = ValorationFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return self.session.execute(query).scalars().all()
   
    def get_valoration_by_teacher_id(self, teacher_id: str) :
        query = select(TeacherNoteTable.teacher_id , TeacherNoteTable.subject_id, (func.sum(TeacherNoteTable.grade)/func.count()).label("valoration")) 
        query = query.group_by(TeacherNoteTable.teacher_id , TeacherNoteTable.subject_id)
        query = query.where(TeacherNoteTable.teacher_id == teacher_id)
        return self.session.execute(query).all()
    

