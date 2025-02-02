from sqlalchemy.orm import Session
from backend.domain.schemas.my_date import DateCreateModel
from backend.domain.models.tables import MyDateTable
import uuid
from .. import IRepository

class DateRepository(IRepository[DateCreateModel,MyDateTable, None,None]):
    def __init__(self, session):    
        super().__init__(session)

    def create(self, entity: DateCreateModel) -> MyDateTable :
        date_dict = entity.model_dump()
        new_date = MyDateTable(**date_dict)
        self.session.add(new_date)
        self.session.commit()
        return new_date
    
    def get(self, filter_params: None) -> list[MyDateTable] :
        pass

    def update(self, changes : None , entity : MyDateTable) -> MyDateTable:
        pass

    def delete(self, entity: MyDateTable) -> None :
        pass

    def get_by_id(self, id: str ) -> MyDateTable :
        query = self.session.query(MyDateTable).filter(MyDateTable.entity_id == id)

        result = query.scalar()

        return result

