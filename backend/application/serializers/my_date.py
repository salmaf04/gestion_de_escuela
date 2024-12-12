from backend.domain.schemas.my_date import DateModel
from backend.domain.models.tables import MyDateTable

class DateMapper() :

    def to_api(self, my_date: MyDateTable) -> DateModel :
        return DateModel(
            id=my_date.entity_id,
            date = my_date.date
        )