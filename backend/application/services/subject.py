from sqlalchemy.orm import Session
from sqlalchemy import select, update
from backend.domain.filters.subject import SubjectFilterSet , SubjectFilterSchema, SubjectChangeRequest
from backend.domain.schemas.subject import SubjectCreateModel, SubjectModel
from backend.domain.models.tables import SubjectTable
import uuid
from backend.application.services.classroom import ClassroomPaginationService
from backend.application.services.course import CoursePaginationService

class SubjectCreateService :

    def create_subject(self, session: Session, subject:SubjectCreateModel) -> SubjectTable :
        course_pagination_service = CoursePaginationService()
        course = course_pagination_service.get_course_by_year(session=session, year=subject.course_year)
        course_id = course.entity_id
        classroom_service = ClassroomPaginationService()
        classroom = classroom_service.get_classroom_by_id(session=session, id=subject.classroom_id)
         
        subject_dict = subject.model_dump()
        new_subject = SubjectTable(**subject_dict, course_id=course_id)
        new_subject.classroom = classroom
        classroom.subjects.append(new_subject)
        session.add(new_subject)
        session.commit()
        return new_subject


class SubjectDeletionService:
    def delete_subject(self, session: Session, subject: SubjectModel) -> None :
        session.delete(subject)
        session.commit()
        

class SubjectUpdateService :
    def update_one(self, session : Session , changes : SubjectChangeRequest , subject : SubjectModel ) -> SubjectModel: 
        query = update(SubjectTable).where(SubjectTable.entity_id == subject.id)
 
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        session.execute(query)
        session.commit()
        
        subject = subject.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return subject
           

class SubjectPaginationService :
    
    def get_subject_by_id(self, session: Session, id:uuid.UUID ) -> SubjectTable :
        query = session.query(SubjectTable).filter(SubjectTable.entity_id == id)

        result = query.scalar()

        return result
    
    def get_subjects(self, session: Session, filter_params: SubjectFilterSchema) -> list[SubjectTable] :
        query = select(SubjectTable)
        filter_set = SubjectFilterSet(session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return session.execute(query).scalars().all()
    