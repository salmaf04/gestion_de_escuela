from .base import IRepository

from sqlalchemy.orm import Session
from sqlalchemy import select, update , and_
from backend.domain.filters.course import  CourseChangeRequest, CourseFilterSchema, CourseFilterSet
from backend.domain.schemas.course import CourseCreateModel, CourseModel
from backend.domain.models.tables import CourseTable

import uuid

class CourseRepository(IRepository[CourseCreateModel,CourseModel, CourseChangeRequest,CourseFilterSchema]):
    """
    Repository for managing courses in the database.
    Extends IRepository with specific implementations for course operations.
    """
    def __init__(self, session):
        """Initialize repository with database session."""
        super().__init__(session)

    def create(self, entity: CourseCreateModel) -> CourseModel:
        """
        Create a new course in the database.
        Args:
            entity: CourseCreateModel containing course details
        Returns:
            Created CourseModel instance
        """
        course_dict = entity.model_dump()
        new_course = CourseTable(**course_dict)
        self.session.add(new_course)
        self.session.commit()
        return new_course
    
    def delete(self, entity: CourseModel) -> None:
        """
        Delete a course from the database.
        Args:
            entity: CourseModel instance to be deleted
        """
        self.session.delete(entity)
        self.session.commit()

    def update(self, changes: CourseChangeRequest, entity: CourseModel) -> CourseModel:
        """
        Update a course's information.
        Args:
            changes: CourseChangeRequest containing fields to update
            entity: Current CourseModel to be updated
        Returns:
            Updated CourseModel instance
        Note: There appears to be a bug where 'student' is used instead of 'course' in the return
        """
        query = update(CourseTable).where(CourseTable.entity_id == entity.id)
        query = query.values(changes.model_dump(exclude_unset=True, exclude_none=True))
        self.session.execute(query)
        self.session.commit()
        
        # Bug: This should be 'course' instead of 'student'
        student = student.model_copy(update=changes.model_dump(exclude_unset=True, exclude_none=True))
        return student
    
    def get_by_id(self, id: str) -> CourseModel:
        """
        Retrieve a course by its ID.
        Args:
            id: String identifier of the course
        Returns:
            Matching CourseModel instance or None
        """
        query = self.session.query(CourseTable).filter(CourseTable.entity_id == id)
        result = query.scalar()
        return result
     
    def get(self, filter_params: CourseFilterSchema) -> list[CourseTable]:
        """
        Retrieve courses based on filter parameters.
        Args:
            filter_params: Filter criteria for courses
        Returns:
            List of matching CourseTable instances
        """
        query = select(CourseTable)
        filter_set = CourseFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return self.session.execute(query).scalars().all()
    
    def get_course_by_year(self, year: int) -> CourseTable:
        """
        Retrieve a course by its academic year.
        Args:
            year: Integer representing the academic year
        Returns:
            Matching CourseTable instance or None
        """
        query = self.session.query(CourseTable).filter(CourseTable.year == year)
        result = query.scalar()
        return result