from backend.domain.schemas.my_date import DateModel
from backend.domain.models.tables import MyDateTable

"""
This module defines a mapper for converting date data into API representations.

Classes:
    DateMapper: A utility class for mapping MyDateTable objects to DateModel objects.

Class Details:

DateMapper:
    - This class provides a method to convert a MyDateTable object, which represents a database record, into a DateModel object, which is used in the API layer.
    
    Methods:
        - to_api(my_date: MyDateTable) -> DateModel: 
            Converts the given MyDateTable object into a DateModel object, mapping the relevant fields such as ID and date.

Dependencies:
    - DateModel for API data representation.
    - MyDateTable for database representation.
"""
class DateMapper() :

    def to_api(self, my_date: MyDateTable) -> DateModel :
        return DateModel(
            id=my_date.entity_id,
            date = my_date.date
        )