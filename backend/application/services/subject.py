from sqlalchemy.orm import Session
from sqlalchemy import select, update
from backend.domain.filters.subject import SubjectFilterSet , SubjectFilterSchema, ChangeRequest
from backend.domain.schemas.subject import SubjectCreateModel, SubjectModel
from backend.domain.models.tables import SubjectTable
import uuid


class SubjectCreateService :

    def create_subject(self, session: Session, subject:SubjectCreateModel) -> SubjectTable :
        subject_dict = subject.model_dump()
        new_subject = SubjectTable(**subject_dict)
        session.add(new_subject)
        session.commit()
        return new_subject


class SubjectDeletionService:
    def delete_subject(self, session: Session, subject: SubjectModel) -> None :
        session.delete(subject)
        session.commit()
        

class SubjectUpdateService :
    def update_one(self, session : Session , changes : ChangeRequest , subject : SubjectModel ) -> SubjectModel: 
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
    