from sqlalchemy.orm import Session
from backend.domain.schemas.valoration import ValorationCreateModel
from backend.domain.models.tables import TeacherNoteTable, TeacherTable, StudentTable, SubjectTable, CourseTable
from backend.application.services.student import StudentPaginationService
from backend.application.services.subject import SubjectPaginationService
from backend.application.services.teacher import TeacherPaginationService
from backend.application.services.course import CoursePaginationService
from backend.domain.filters.valoration import ValorationFilterSchema, ValorationFilterSet
from sqlalchemy import select, func, update
from backend.infrastructure.repositories.valoration import ValorationRepository

class ValorationCreateService :
    def __init__(self, session):
        self.repo_instance = ValorationRepository(session)
        self.teacher_pagination_service = TeacherPaginationService(session)
        self.student_pagination_service = StudentPaginationService(session)
        self.subject_pagination_service = SubjectPaginationService(session)
        self.course_pagination_service = CoursePaginationService(session)

    def create_valoration(
        self, 
        valoration: ValorationCreateModel,
    ) -> TeacherNoteTable : 
        return self.repo_instance.create(
            valoration=valoration,
            student=self.student_pagination_service.get_student_by_id(id=valoration.student_id),
            subject=self.subject_pagination_service.get_subject_by_id(id=valoration.subject_id),
            teacher=self.teacher_pagination_service.get_teacher_by_id(id=valoration.teacher_id),
            course=self.course_pagination_service.get_course_by_id(id=valoration.course_id)
        )
        
class ValorationPaginationService :
    def __init__(self, session):
        self.repo_instance = ValorationRepository(session)

    def get_valoration(self, filter_params: ValorationFilterSchema) -> list[TeacherNoteTable] :
        return self.repo_instance.get(filter_params)
        

    def get_valoration_by_teacher_id(self, teacher_id: str) :
        return self.repo_instance.get_valoration_by_teacher_id(teacher_id)
