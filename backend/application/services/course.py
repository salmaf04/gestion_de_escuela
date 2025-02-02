from sqlalchemy.orm import Session
from sqlalchemy import select, update , and_
from backend.domain.filters.course import  CourseChangeRequest, CourseFilterSchema, CourseFilterSet
from backend.domain.schemas.course import CourseCreateModel, CourseModel
from backend.domain.models.tables import CourseTable

import uuid


class CourseCreateService :

    def create_course(self, session: Session, course:CourseCreateModel) -> CourseTable :
        course_dict = course.model_dump()
        new_course = CourseTable(**course_dict)
        session.add(new_course)
        session.commit()
        return new_course


class CourseDeletionService:
    def delete_course(self, session: Session, course: CourseModel) -> None :
        session.delete(course)
        session.commit()
        

class CourseUpdateService :
    def update_one(self, session : Session , changes : CourseChangeRequest , course : CourseModel ) -> CourseModel: 
        query = update(CourseTable).where(CourseTable.entity_id == course.id)
        
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        session.execute(query)
        session.commit()
        
        student = student.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return student
           

class CoursePaginationService :
        
    def get_course_by_id(self, session: Session, id:uuid.UUID ) -> CourseTable :
        query = session.query(CourseTable).filter(CourseTable.entity_id == id)

        result = query.scalar()

        return result
    
    def get_course_by_year(self, session: Session, year: int) -> CourseTable :
        query = session.query(CourseTable).filter(CourseTable.year == year)
        result = query.scalar()
        return result
    
    def get_course(self, session: Session, filter_params: CourseFilterSchema) -> list[CourseTable] :
        query = select(CourseTable)
        filter_set = CourseFilterSet(session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return session.execute(query).scalars().all()