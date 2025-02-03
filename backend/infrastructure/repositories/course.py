from .base import IRepository

from sqlalchemy.orm import Session
from sqlalchemy import select, update , and_
from backend.domain.filters.course import  CourseChangeRequest, CourseFilterSchema, CourseFilterSet
from backend.domain.schemas.course import CourseCreateModel, CourseModel
from backend.domain.models.tables import CourseTable

import uuid

class CourseRepository(IRepository[CourseCreateModel,CourseModel, CourseChangeRequest,CourseFilterSchema]):
    def __init__(self, session):
        super().__init__(session)

    def create(self, entity: CourseCreateModel) -> CourseModel:
        course_dict = entity.model_dump()
        new_course = CourseTable(**course_dict)
        self.session.add(new_course)
        self.session.commit()
        return new_course
    
    def delete(self, entity: CourseModel) -> None:
        self.session.delete(entity)
        self.session.commit()

    def update(self, changes: CourseChangeRequest, entity: CourseModel) -> CourseModel:
        query = update(CourseTable).where(CourseTable.entity_id == entity.id)
        
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        self.session.execute(query)
        self.session.commit()
        
        student = student.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return student
    
    def get_by_id (self, id: str) -> CourseModel:
        query = self.session.query(CourseTable).filter(CourseTable.entity_id == id)

        result = query.scalar()

        return result
     
    def get(self , filter_params: CourseFilterSchema) -> list[CourseTable] :
        query = select(CourseTable)
        filter_set = CourseFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return self.session.execute(query).scalars().all()
    
    def get_course_by_year(self, year: int) -> CourseTable :
        query = self.session.query(CourseTable).filter(CourseTable.year == year)
        result = query.scalar()
        return result