from sqlalchemy.orm import Session
from backend.domain.schemas.my_date import DateCreateModel
from backend.domain.models.tables import MyDateTable
import uuid
from backend.infrastructure.repositories.my_date import DateRepository

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