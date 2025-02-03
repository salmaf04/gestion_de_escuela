from backend.domain.schemas.classroom import ClassroomCreateModel, ClassroomModel
from backend.domain.models.tables import ClassroomTable, MeanTable
from sqlalchemy.orm import Session
from backend.domain.filters.classroom import ClassroomFilterSchema, ClassroomFilterSet, ClassroomChangeRequest
from sqlalchemy import select, update
import uuid
from backend.infrastructure.repositories.classroom import ClassroomRepository

"""
This module defines services for creating, retrieving, updating, and deleting classroom records.

Classes:
    ClassroomCreateService: A service for creating new classroom records.
    ClassroomDeletionService: A service for deleting classroom records.
    ClassroomUpdateService: A service for updating classroom records.
    ClassroomPaginationService: A service for retrieving classroom records based on various criteria.

Classes Details:

1. ClassroomCreateService:
    - This service is responsible for creating new classroom records.
    - It utilizes the ClassroomRepository to interact with the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - create_classroom(classroom: ClassroomCreateModel) -> ClassroomTable: 
            Creates a new classroom record using the provided ClassroomCreateModel and returns the created ClassroomTable object.

2. ClassroomDeletionService:
    - This service is responsible for deleting classroom records.
    - It uses the ClassroomRepository to perform deletion operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - delete_classroom(classroom: ClassroomModel) -> None: 
            Deletes the specified classroom record.

3. ClassroomUpdateService:
    - This service is responsible for updating classroom records.
    - It uses the ClassroomRepository to perform update operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - update_one(changes: ClassroomChangeRequest, classroom: ClassroomModel) -> ClassroomModel: 
            Updates the specified classroom record with the provided changes and returns the updated ClassroomModel.

4. ClassroomPaginationService:
    - This service is responsible for retrieving classroom records based on different criteria.
    - It uses the ClassroomRepository to fetch data from the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - get_classroom_by_id(id: uuid.UUID) -> ClassroomTable: 
            Retrieves a classroom record by the specified ID.
        - get_classroom(filter_params: ClassroomFilterSchema): 
            Retrieves a list of classrooms based on the provided filter parameters.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - ClassroomRepository for database operations related to classrooms.
    - ClassroomCreateModel, ClassroomModel, ClassroomTable, and other domain models for data representation.
    - ClassroomFilterSchema and ClassroomFilterSet for filtering classroom records.
    - UUID for handling unique identifiers.
"""

class ClassroomCreateService :
    def __init__(self, session):
        self.repo_instance = ClassroomRepository(session)

    def create_classroom(self, classroom: ClassroomCreateModel) -> ClassroomTable :
        return self.repo_instance.create(classroom)
class ClassroomDeletionService:
    def __init__ (self, session):
        self.repo_instance = ClassroomRepository(session)

    def delete_classroom(self, classroom: ClassroomModel) -> None :
        return self.repo_instance.delete(classroom)
        
class ClassroomUpdateService :
    def __init__ (self, session):
        self.repo_instance = ClassroomRepository(session)

    def update_one(self, changes : ClassroomChangeRequest , classroom : ClassroomModel ) -> ClassroomModel: 
        return self.repo_instance.update(changes, classroom)
class ClassroomPaginationService :
    def __init__ (self, session):
        self.repo_instance = ClassroomRepository(session)

    def get_classroom_by_id(self, id:uuid.UUID ) -> ClassroomTable :
        return self.repo_instance.get_by_id(id)
    
    def get_classroom(self, filter_params: ClassroomFilterSchema)  :
        return self.repo_instance.get(filter_params)
