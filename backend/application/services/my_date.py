from sqlalchemy.orm import Session
from backend.domain.schemas.course import DateCreateModel
from backend.domain.models.tables import MyDateTable
import uuid

class DateCreateService :

    def create_date(self, session: Session, date:DateCreateModel) -> MyDateTable :
        date_dict = date.model_dump()
        new_date = MyDateTable(**date_dict)
        session.add(new_date)
        session.commit()
        return new_date
    
    
class DatePaginationService :
        
    def get_date_by_id(self, session: Session, id:uuid.UUID ) -> MyDateTable :
        query = session.query(MyDateTable).filter(MyDateTable.entity_id == id)

        result = query.scalar()

        return result