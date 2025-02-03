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
from  backend.infrastructure.repositories.absence import AbsenceRepository

class AbsenceCreateService :
    def __init__(self, session):
        self.repo_instance = AbsenceRepository(session)

    def create_absence(self, absence:AbsenceCreateModel) -> AbsenceTable :
        return self.repo_instance.create(absence)
    
class AbsencePaginationService :
    def __init__(self, session):
        self.repo_instance = AbsenceRepository(session)

    def get_absence(self, filter_params: AbsenceFilterSchema) -> list[AbsenceTable] :
        return self.repo_instance.get(filter_params)
    
    def get_absence_by_student(self,  student_id: uuid.UUID) -> list[AbsenceTable] :
        return self.repo_instance.get_absence_by_student(student_id)
    
    def get_absence_by_student_by_teacher(self, teacher_id: uuid.UUID) -> list[AbsenceTable] :
        return self.repo_instance.get_absence_by_student_by_teacher(teacher_id)

