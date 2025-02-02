from sqlalchemy.orm import Session
from backend.domain.schemas.valoration import ValorationCreateModel
from backend.domain.models.tables import TeacherNoteTable, TeacherTable
from backend.application.services.student import StudentPaginationService
from backend.application.services.subject import SubjectPaginationService
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.course import CoursePaginationService
from backend.domain.filters.valoration import ValorationFilterSchema, ValorationFilterSet
from sqlalchemy import select, func, update

class ValorationCreateService :
    def create_valoration(self, session: Session, valoration: ValorationCreateModel) -> TeacherNoteTable : 
        valoration_dict = valoration.model_dump()
        new_valoration = TeacherNoteTable(**valoration_dict)
        
        student = StudentPaginationService().get_student_by_id(session=session, id=valoration.student_id)
        subject = SubjectPaginationService().get_subject_by_id(session=session, id=valoration.subject_id)
        teacher = TeacherPaginationService().get_teacher_by_id(session=session, id=valoration.teacher_id)
        course = CoursePaginationService().get_course_by_id(session=session, id=valoration.course_id)

        new_valoration.student = student
        new_valoration.subject = subject  
        new_valoration.teacher = teacher
        new_valoration.course = course

        teacher.teacher_note_association.append(new_valoration)
        subject.teacher_note_association.append(new_valoration)
        student.teacher_note_association.append(new_valoration)
        course.teacher_note_association.append(new_valoration)

        session.add(new_valoration)
        session.commit()
        return new_valoration
    
class ValorationPaginationService :
    def get_valoration(self, session: Session, filter_params: ValorationFilterSchema) -> list[TeacherNoteTable] :
        query = select(TeacherNoteTable)
        filter_set = ValorationFilterSet(session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return session.execute(query).scalars().all()
    

    def get_valoration_by_teacher_id(self, session: Session, teacher_id: str) :
        query = select(TeacherNoteTable.teacher_id , TeacherNoteTable.subject_id, (func.sum(TeacherNoteTable.grade)/func.count()).label("valoration")) 
        query = query.group_by(TeacherNoteTable.teacher_id , TeacherNoteTable.subject_id)
        query = query.where(TeacherNoteTable.teacher_id == teacher_id)
        return session.execute(query).all()
    

class ValorationCheckService :
    def update_valoration(self, session: Session) :
        query = update(TeacherNoteTable).values(less_than_three_valoration=TeacherNoteTable.less_than_three_valoration + 1)
        query = query.where(TeacherTable.average_valoration < 3)
        session.execute(query)
        session.commit()