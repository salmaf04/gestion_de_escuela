from sqlalchemy.orm import Session
from backend.application.serializers.teacher import TeacherMapper
from backend.domain.schemas.teacher import TeacherCreateModel, TeacherModel
from backend.domain.models.tables import TeacherTable, teacher_subject_table, TeacherNoteTable, UserTable
from sqlalchemy import and_, update
import uuid
from sqlalchemy import select
from backend.domain.filters.teacher import TeacherFilterSet , TeacherFilterSchema, ChangeRequest
from backend.domain.filters.subject import SubjectFilterSchema
from ..utils.auth import get_password_hash, get_password
from backend.application.services.subject import SubjectPaginationService
from sqlalchemy import func


class TeacherCreateService :

    def create_teacher(self, session: Session, teacher: TeacherCreateModel) -> TeacherTable :
        subject_service = SubjectPaginationService()
        subjects = subject_service.get_subjects(session=session, filter_params=SubjectFilterSchema(name=teacher.list_of_subjects))
        teacher_dict = teacher.model_dump(exclude={'password', 'list_of_subjects'})
        hashed_password = get_password_hash(get_password(teacher))
        new_teacher = TeacherTable(**teacher_dict, hash_password=hashed_password)
        new_teacher.teacher_subject_association = subjects
        session.add(new_teacher)
        session.commit()
        for subject in subjects :
            subject.teacher_subject_association.append(new_teacher)
        return new_teacher
    
    
class TeacherDeletionService:
    def delete_teacher(self, session: Session, teacher: TeacherModel) -> None :
        session.delete(teacher)
        session.commit()
        
       
class TeacherUpdateService :
    pass
    """ 
    def update_one(self, session : Session , changes : ChangeRequest , teacher : TeacherModel ) -> TeacherModel: 
        print(changes.hash_password)
        if changes.hash_password :
            print(changes.hash_password)
            hashed_password = get_password_hash(changes.hash_password)
            changes.hash_password = hashed_password
            print(changes.hash_password)
            print(changes.model_dump(exclude_unset=True, exclude_none=True))
        
        #query = update(TeacherTable).values(changes.model_dump(exclude_unset=True, exclude_none=True)).where(TeacherTable.id == teacher.id)
        query = update(TeacherTable).values(changes.model_dump(exclude_unset=True, exclude_none=True))
        query = query.where(TeacherTable.id == UserTable.entity_id)
        query = query.where(
        session.execute(query)
        session.refresh(teacher)
        
        teacher = teacher.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return teacher
        """
        

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
        teachers = session.scalars(query).all()
        valoration_service = TeacherValorationService()
        mapper = TeacherMapper()
        valorations = []
        subjects = []

        if teachers :
            for teacher in teachers :
                valorations.append(valoration_service.get_teacher_valoration_average(session=session, teacher_id=teacher.id))
                subjects.append(mapper.to_subject_list(teacher.teacher_subject_association))

        return teachers, valorations, subjects


    
class TeacherSubjectService :
    def create_teacher_subject(self, session: Session, teacher_id: str, subject_id: str) :
        teacher_subject = teacher_subject_table.insert().values(teacher_id=teacher_id, subject_id=subject_id)
        session.execute(teacher_subject)
        session.commit()

class TeacherValorationService :
    def get_teacher_valoration_average(self, session: Session, teacher_id: str)  :
        value = select(func.sum(TeacherNoteTable.grade)).where(TeacherNoteTable.teacher_id == teacher_id)
        valoration_sum = session.execute(value).scalars().first()
        if valoration_sum is None :
            return None
        rows = select(func.count(TeacherNoteTable.grade)).where(TeacherNoteTable.teacher_id == teacher_id)
        total_valorations = session.execute(rows).scalars().first()
        return valoration_sum / total_valorations
    
class TeacherSubjectService :
    def get_teacher_subjects(self, session: Session, id:uuid.UUID ) -> list[str] :
        query = select(TeacherTable).where(TeacherTable.entity_id == id)
        teacher = session.execute(query).scalars().first()
        subjects = teacher.teacher_subject_association
        return TeacherMapper().to_subject_list(subjects)
        
        