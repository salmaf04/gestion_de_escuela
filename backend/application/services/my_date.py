from sqlalchemy.orm import Session
from backend.domain.schemas.my_date import DateCreateModel
from backend.domain.models.tables import MyDateTable
import uuid
from backend.infrastructure.repositories.my_date import DateRepository

"""
This module defines services for creating and retrieving date records.

Classes:
    DateCreateService: A service for creating new date records.
    DatePaginationService: A service for retrieving date records based on specific criteria.

Classes Details:

1. DateCreateService:
    - This service is responsible for creating new date records.
    - It utilizes the DateRepository to interact with the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - create_date(date: DateCreateModel) -> MyDateTable: 
            Creates a new date record using the provided DateCreateModel and returns the created MyDateTable object.

2. DatePaginationService:
    - This service is responsible for retrieving date records based on specific criteria.
    - It uses the DateRepository to fetch data from the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - get_date_by_id(id: uuid.UUID) -> MyDateTable: 
            Retrieves a date record by the specified ID.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - DateRepository for database operations related to dates.
    - DateCreateModel and MyDateTable for data representation.
    - UUID for handling unique identifiers.
"""
class DateCreateService :
    def __init__(self, session):
        self.repo_instance = DateRepository(session)

    def create_date(self, date:DateCreateModel) -> MyDateTable :
        return self.repo_instance.create(date)
    
class DatePaginationService :
    def __init__(self, session):    
        self.repo_instance = DateRepository(session)
        
    def get_date_by_id(self, id:uuid.UUID ) -> MyDateTable :
        return self.repo_instance.get_by_id(id)