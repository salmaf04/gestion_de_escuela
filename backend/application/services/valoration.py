from sqlalchemy.orm import Session
from backend.domain.schemas.valoration import ValorationCreateModel
from backend.domain.models.tables import TeacherNoteTable
from backend.application.services.student import StudentPaginationService
from backend.application.services.subject import SubjectPaginationService
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.course import CoursePaginationService

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

        teacher.student_valoration_association.append(new_valoration)
        subject.student_teacher_association.append(new_valoration)
        student.student_valoration_association.append(new_valoration)
        course.course_valoration_association.append(new_valoration)

        session.add(new_valoration)
        session.commit()
        return new_valoration