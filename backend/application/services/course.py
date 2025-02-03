from sqlalchemy.orm import Session
from sqlalchemy import select, update , and_
from backend.domain.filters.course import  CourseChangeRequest, CourseFilterSchema, CourseFilterSet
from backend.domain.schemas.course import CourseCreateModel, CourseModel
from backend.domain.models.tables import CourseTable
from backend.infrastructure.repositories.course import CourseRepository
import uuid

"""
This module defines services for creating, retrieving, updating, and deleting course records.

Classes:
    CourseCreateService: A service for creating new course records.
    CourseDeletionService: A service for deleting course records.
    CourseUpdateService: A service for updating course records.
    CoursePaginationService: A service for retrieving course records based on various criteria.

Classes Details:

1. CourseCreateService:
    - This service is responsible for creating new course records.
    - It utilizes the CourseRepository to interact with the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - create_course(course: CourseCreateModel) -> CourseTable: 
            Creates a new course record using the provided CourseCreateModel and returns the created CourseTable object.

2. CourseDeletionService:
    - This service is responsible for deleting course records.
    - It uses the CourseRepository to perform deletion operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - delete_course(course: CourseModel) -> None: 
            Deletes the specified course record.

3. CourseUpdateService:
    - This service is responsible for updating course records.
    - It uses the CourseRepository to perform update operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - update_one(changes: CourseChangeRequest, course: CourseModel) -> CourseModel: 
            Updates the specified course record with the provided changes and returns the updated CourseModel.

4. CoursePaginationService:
    - This service is responsible for retrieving course records based on different criteria.
    - It uses the CourseRepository to fetch data from the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - get_course_by_id(id: uuid.UUID) -> CourseTable: 
            Retrieves a course record by the specified ID.
        - get_course_by_year(year: int) -> CourseTable: 
            Retrieves a course record by the specified year.
        - get_course(filter_params: CourseFilterSchema) -> list[CourseTable]: 
            Retrieves a list of courses based on the provided filter parameters.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - CourseRepository for database operations related to courses.
    - CourseCreateModel, CourseModel, CourseTable, and other domain models for data representation.
    - CourseFilterSchema and CourseFilterSet for filtering course records.
    - UUID for handling unique identifiers.
"""

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