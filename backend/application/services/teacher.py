from sqlalchemy.orm import Session
from backend.domain.schemas.teacher import TeacherCreateModel, TeacherModel
from backend.domain.models.tables import TeacherTable
from sqlalchemy import and_, update
import uuid
from sqlalchemy import select
from backend.domain.filters.teacher import TeacherFilterSet , TeacherFilterSchema, ChangeRequest
from ..utils.auth import get_password_hash


class TeacherCreateService :

    def create_teacher(self, session: Session, teacher: TeacherCreateModel) -> TeacherTable :
        teacher_dict = teacher.model_dump(exclude={'password'})
        hashed_password = get_password_hash(teacher.password)
        new_teacher = TeacherTable(**teacher_dict, hash_password=hashed_password)
        session.add(new_teacher)
        session.commit()
        return new_teacher
    
    
class TeacherDeletionService:
    def delete_teacher(self, session: Session, teacher: TeacherModel) -> None :
        session.delete(teacher)
        session.commit()
        
        
class TeacherUpdateService :
    def update_one(self, session : Session , changes : ChangeRequest , teacher : TeacherModel ) -> TeacherModel: 
        query = update(TeacherTable).where(TeacherTable.entity_id == teacher.id)
        
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        session.execute(query)
        session.commit()
        
        teacher = teacher.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return teacher
        

class TeacherPaginationService :
    def get_teacher_by_email(self, session: Session, email: str) -> TeacherTable :
        query = session.query(TeacherTable).filter(TeacherTable.email == email)

        result = query.first()

        return result
    
    def get_teacher_by_id(self, session: Session, id:uuid.UUID ) -> TeacherTable :
        query = session.query(TeacherTable).filter(TeacherTable.entity_id == id)

        result = query.scalar()

        return result
    
    def get_teachers(self, session: Session, filter_params: TeacherFilterSchema) -> list[TeacherTable] :
        query = select(TeacherTable)
        filter_set = TeacherFilterSet(session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return session.scalars(query).all()
    





    




 