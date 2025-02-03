from sqlalchemy.orm import Session
from sqlalchemy import func, asc, distinct
from backend.application.serializers.teacher import TeacherMapper
from backend.domain.schemas.teacher import TeacherCreateModel, TeacherModel
from backend.domain.models.tables import TeacherTable, teacher_subject_table, TeacherNoteTable, UserTable, SanctionTable
from sqlalchemy import and_, update
import uuid
from sqlalchemy import select
from backend.domain.filters.teacher import TeacherFilterSet , TeacherFilterSchema, TeacherChangeRequest
from backend.domain.filters.subject import SubjectFilterSchema
from ..utils.auth import get_password_hash, get_password
from backend.application.services.subject import SubjectPaginationService
from sqlalchemy import func
from backend.application.utils.valoration_average import get_teacher_valoration_average, calculate_teacher_average
from backend.domain.models.tables import ClassroomTable, TechnologicalMeanTable, SubjectTable, teacher_subject_table
from sqlalchemy.orm import aliased
from fastapi import HTTPException, status
from backend.infrastructure.repositories.teacher import TeacherRepository
class TeacherCreateService :
    def __init__ (self, session):
        self.repo_istance = TeacherRepository(session)
        self.subject_pagination = SubjectPaginationService(session)
    
    def create_teacher(self, teacher: TeacherCreateModel) -> TeacherTable :
        subjects = self.subject_pagination.get_subjects(filter_params=SubjectFilterSchema(name=teacher.list_of_subjects))
        return self.repo_istance.create(teacher, subjects=subjects)
class TeacherDeletionService:
    def __init__ (self, session):
        self.repo_istance = TeacherRepository(session)

    def delete_teacher(self, teacher: TeacherModel) -> None :
        return self.repo_istance.delete(teacher)

class TeacherUpdateService :
    def __init__(self, session):
        self.repo_istance = TeacherRepository(session)

    def update(self, changes : TeacherChangeRequest , teacher : TeacherModel ) -> TeacherModel: 
        return self.repo_istance.update(changes, teacher)
        
class TeacherPaginationService :
    def __init__(self, session):
        self.repo_istance = TeacherRepository(session)

    def get_teacher_by_email(self, email: str) -> TeacherTable :
        self.repo_istance.get_teacher_by_email(email)
       
    def get_teacher_by_id(self, id:uuid.UUID ) -> TeacherTable :
        return self.repo_istance.get_by_id(id)
        
    def get_teachers(self, filter_params: TeacherFilterSchema) -> list[TeacherTable] :
        return self.repo_istance.get(filter_params)
        
    def get_teachers_average_better_than_8(self) :
        return self.repo_istance.get_teachers_average_better_than_8()

    def get_teachers_by_technological_classroom(self) : 
        return self.repo_istance.get_teachers_by_technological_classroom()
    
    def get_teachers_by_sanctions(self) :
        return self.repo_istance.get_teachers_by_sanctions()
        
class TeacherSubjectService :
    def create_teacher_subject(self, session: Session, teacher_id: str, subject_id: str) :
        teacher_subject = teacher_subject_table.insert().values(teacher_id=teacher_id, subject_id=subject_id)
        session.execute(teacher_subject)
        session.commit()
class TeacherSubjectService :
    def __init__ (self, session) :
        self.repo_instance = TeacherRepository(session)

    def get_teacher_subjects(self, id:uuid.UUID ) -> list[str] :
        return self.repo_instance.get_teacher_subjects(id)
        