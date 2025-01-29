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

class TeacherCreateService :

    def create_teacher(self, session: Session, teacher: TeacherCreateModel) -> TeacherTable :
        subject_service = SubjectPaginationService()
        subjects = subject_service.get_subjects(session=session, filter_params=SubjectFilterSchema(name=teacher.list_of_subjects))
        self.check_subject(subjects, teacher.list_of_subjects)
        teacher_dict = teacher.model_dump(exclude={'password', 'list_of_subjects'})
        hashed_password = get_password_hash(get_password(teacher))
        new_teacher = TeacherTable(**teacher_dict, hash_password=hashed_password)
        new_teacher.teacher_subject_association = subjects
        session.add(new_teacher)
        session.commit()
        for subject in subjects :
            subject.teacher_subject_association.append(new_teacher)
        return new_teacher
    
    
    def check_subject(self,subjects_in_table, subjects_in_request):
        subjects_in_table_names = [subject.name for subject in subjects_in_table]
        subjects_in_table_names.sort()
        subjects_in_request.sort()
        wrong_subjects = []
        print(subjects_in_table_names)
        print(subjects_in_request)

        for subject_in_table, subject_in_request in zip(subjects_in_table_names, subjects_in_request):
            if subject_in_table != subject_in_request:
                wrong_subjects.append(subject_in_request)
            
        if wrong_subjects:
            wrong_subjects_str = ', '.join(wrong_subjects)
            if len(wrong_subjects) == 1:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Está intentando crear un nuevo profesor con una asignatura no válida: {wrong_subjects_str}"
                )
            raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Está intentando crear un nuevo profesor con asignaturas no válidas: {wrong_subjects_str}"
                )
class TeacherDeletionService:
    def delete_teacher(self, session: Session, teacher: TeacherModel) -> None :
        session.delete(teacher)
        session.commit()


class TeacherUpdateService :
    def update_one(self, session : Session , changes : TeacherChangeRequest , teacher : TeacherModel ) -> TeacherModel: 
        query = update(TeacherTable).where(TeacherTable.entity_id == teacher.id)
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        session.execute(query)
        session.commit()
            
        teacher = teacher.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return teacher
            


""" 
class TeacherUpdateService :
    
   
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
        mapper = TeacherMapper()
        subjects = []
 
        if teachers :
            for teacher in teachers :
                subjects.append(mapper.to_subject_list(teacher.teacher_subject_association))

        return teachers, subjects
    

    def get_teachers_average_better_than_8(self, session: Session) :
        subjects = []
        query = select(TeacherTable.name, TeacherTable.id, TeacherTable.average_valoration).where(TeacherTable.average_valoration > 8)
        results = session.execute(query).all()
        mapper = TeacherMapper()

        for teacher in results :
            teacher = self.get_teacher_by_id(session=session, id=teacher.id)
            subjects.append(mapper.to_subject_list(teacher.teacher_subject_association))

        return results, subjects
    

    def get_teachers_by_technological_classroom(self, session: Session) : 
        query = select(TeacherTable, SubjectTable, ClassroomTable, TechnologicalMeanTable.name, TechnologicalMeanTable.state)   
        query = query.join(teacher_subject_table, TeacherTable.id == teacher_subject_table.c.teacher_id)
        query = query.join(SubjectTable, teacher_subject_table.c.subject_id == SubjectTable.entity_id)
        query = query.join(ClassroomTable, SubjectTable.classroom_id == ClassroomTable.entity_id)
        query = query.join(TechnologicalMeanTable, ClassroomTable.entity_id == TechnologicalMeanTable.classroom_id)
        query = query.distinct(TechnologicalMeanTable.id,ClassroomTable.entity_id, TeacherTable.id)
        query = query.order_by(asc(TeacherTable.id))
        return session.execute(query).all()
    
    def get_teachers_by_sanctions(self, session: Session) :
        latest_sanction_subquery = (
        select(
            SanctionTable.teacher_id,
            func.max(SanctionTable.date).label('latest_sanction_date')
        )
        .group_by(SanctionTable.teacher_id)
        .subquery()
        )
        grade_rank = func.row_number().over(
        partition_by=TeacherTable.id,
        order_by=asc(TeacherNoteTable.grade)
        ).label('grade_rank')
        query = select(TeacherTable.id, TeacherTable.name, latest_sanction_subquery.c.latest_sanction_date, TeacherNoteTable.grade)
        query = query.add_columns(grade_rank)
        query = query.join(latest_sanction_subquery, TeacherTable.id == latest_sanction_subquery.c.teacher_id)
        query = query.join(TeacherNoteTable, TeacherTable.id == TeacherNoteTable.teacher_id)
        query = query.where(TeacherTable.id.in_(select(SanctionTable.teacher_id)))
        query = query.order_by(
            TeacherTable.id,
            TeacherNoteTable.grade,
        )
        subquery = query.subquery()
        final_query = select(subquery).where(subquery.c.grade_rank <= 3)
        return session.execute(final_query).all(), self.get_teachers_by_technological_classroom(session)
        
class TeacherSubjectService :
    def create_teacher_subject(self, session: Session, teacher_id: str, subject_id: str) :
        teacher_subject = teacher_subject_table.insert().values(teacher_id=teacher_id, subject_id=subject_id)
        session.execute(teacher_subject)
        session.commit()

class TeacherValorationService :
    def update_note_average(self, session: Session, teacher_id: str, new_note : int ) : 
        new_avergage = calculate_teacher_average(session=session, teacher_id=teacher_id, new_note=new_note)
        query = update(TeacherTable).where(TeacherTable.id == teacher_id).values(average_valoration=new_avergage)
        session.execute(query)
        session.commit()
    
class TeacherSubjectService :
    def get_teacher_subjects(self, session: Session, id:uuid.UUID ) -> list[str] :
        query = select(TeacherTable).where(TeacherTable.entity_id == id)
        teacher = session.execute(query).scalars().first()
        subjects = teacher.teacher_subject_association
        return TeacherMapper().to_subject_list(subjects)
        
        