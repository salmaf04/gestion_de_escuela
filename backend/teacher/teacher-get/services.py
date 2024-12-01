from teacher.teacher_common.schemas import TeacherModel
from sqlalchemy.orm import Session
from database.tables import TeacherTable
from sqlalchemy import select
from .filters import TeacherFilterSet , TeacherFilterSchema


class TeacherListingService:
    def get_teachers(self, session: Session, filter_params: TeacherFilterSchema) -> list[TeacherTable] :
        query = select(TeacherTable)
        filter_set = TeacherFilterSet(session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return session.execute(query).scalars().all()


    
    
       
    
         