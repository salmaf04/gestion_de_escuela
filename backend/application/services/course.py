from sqlalchemy.orm import Session
from sqlalchemy import select, update , and_
from backend.domain.filters.course import  CourseChangeRequest, CourseFilterSchema, CourseFilterSet
from backend.domain.schemas.course import CourseCreateModel, CourseModel
from backend.domain.models.tables import CourseTable
from backend.infrastructure.repositories.course import CourseRepository
import uuid


class CourseCreateService :
    def __init__(self, session):
        self.repo_instance = CourseRepository(session)

    def create_course(self, course:CourseCreateModel) -> CourseTable :
        return self.repo_instance.create(course)

class CourseDeletionService:
    def __init__(self, session):
        self.repo_instance = CourseRepository(session)

    def delete_course(self, course: CourseModel) -> None :
        return self.repo_instance.delete(course)
        
class CourseUpdateService :
    def __init__(self, session):
        self.repo_instance = CourseRepository(session)

    def update_one(self, changes : CourseChangeRequest , course : CourseModel ) -> CourseModel: 
        return self.repo_instance.update(changes, course)

class CoursePaginationService :
    def __init__(self, session):
        self.repo_instance = CourseRepository(session)
        
    def get_course_by_id(self, id:uuid.UUID ) -> CourseTable :
        return self.repo_instance.get_by_id(id)
    
    def get_course_by_year(self, year: int) -> CourseTable :
        return self.repo_instance.get_by_year(year)
    
    def get_course(self, filter_params: CourseFilterSchema) -> list[CourseTable] :
        return self.repo_instance.get(filter_params)