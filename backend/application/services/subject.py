from sqlalchemy.orm import Session
from sqlalchemy import select, update
from backend.domain.filters.subject import SubjectFilterSet , SubjectFilterSchema, SubjectChangeRequest
from backend.domain.schemas.subject import SubjectCreateModel, SubjectModel
from backend.domain.models.tables import SubjectTable
import uuid
from backend.application.services.classroom import ClassroomPaginationService
from backend.application.services.course import CoursePaginationService
from backend.infrastructure.repositories.subject import SubjectRepository
class SubjectCreateService :
    def __init__(self, session):
        self.repo_instance = SubjectRepository(session)

    def create_subject(self, subject:SubjectCreateModel) -> SubjectTable :
        return self.repo_instance.create(subject)
    
class SubjectDeletionService:
    def __init__(self, session):
        self.repo_instance = SubjectRepository(session)

    def delete_subject(self, subject: SubjectModel) -> None :
        return self.repo_instance.delete(subject)
        
class SubjectUpdateService :
    def __init__(self, session):
        self.repo_instance = SubjectRepository(session)

    def update_one(self, changes : SubjectChangeRequest , subject : SubjectModel ) -> SubjectModel: 
        return self.repo_instance.update(changes, subject)

class SubjectPaginationService :
    def __init__(self, session):
        self.repo_instance = SubjectRepository(session)
    
    def get_subject_by_id(self, id:uuid.UUID ) -> SubjectTable :
        return self.repo_instance.get_by_id(id)
    
    def get_subjects(self, filter_params: SubjectFilterSchema) -> list[SubjectTable] :
        return self.repo_instance.get(filter_params)
    