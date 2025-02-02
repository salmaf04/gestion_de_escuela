from sqlalchemy import select, update
from backend.domain.filters.subject import SubjectFilterSet , SubjectFilterSchema, SubjectChangeRequest
from backend.domain.schemas.subject import SubjectCreateModel, SubjectModel
from backend.domain.models.tables import SubjectTable
import uuid
from backend.application.services.classroom import ClassroomPaginationService
from backend.application.services.course import CoursePaginationService
from .base import IRepository

class SubjectRepository(IRepository[SubjectCreateModel,SubjectTable, SubjectChangeRequest,SubjectFilterSchema]):
    def __init__(self, session):
        super().__init__(session)

    def create(self, entity: SubjectCreateModel) -> SubjectTable :
        course_pagination_service = CoursePaginationService()
        classroom_service = ClassroomPaginationService()
        classroom = classroom_service.get_classroom_by_id(session=self.session, id=entity.classroom_id)
         
        subject_dict = entity.model_dump()
        new_subject = SubjectTable(**subject_dict)
        new_subject.classroom = classroom
        classroom.subjects.append(new_subject)
        self.session.add(new_subject)
        self.session.commit()
        return new_subject

    def delete(self, entity: SubjectTable) -> None :
        self.session.delete(entity)
        self.session.commit()

    def update(self, changes : SubjectChangeRequest , entity : SubjectTable) -> SubjectTable :
        query = update(SubjectTable).where(SubjectTable.entity_id == entity.entity_id)
 
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        self.session.execute(query)
        self.session.commit()
        
        subject = entity.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return subject
           
    def get_by_id(self, id: str ) -> SubjectTable :
        query = self.session.query(SubjectTable).filter(SubjectTable.entity_id == id)

        result = query.scalar()

        return result
    
    def get(self, filter_params: SubjectFilterSchema) -> list[SubjectTable] :
        query = select(SubjectTable)
        filter_set = SubjectFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return self.session.execute(query).scalars().all()
