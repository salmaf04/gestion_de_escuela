from backend.domain.schemas.mean import MeanModel
from backend.domain.models.tables import MeanTable

"""
This module defines a mapper for converting mean data into API representations.

Classes:
    MeanMapper: A utility class for mapping MeanTable objects to MeanModel objects.

Class Details:

MeanMapper:
    - This class provides a method to convert a MeanTable object, which represents a database record, into a MeanModel object, which is used in the API layer.
    
    Methods:
        - to_api(mean: MeanTable) -> MeanModel: 
            Converts the given MeanTable object into a MeanModel object, mapping the relevant fields such as ID, name, state, location, type, classroom ID, and to_be_replaced status.

Dependencies:
    - MeanModel for API data representation.
    - MeanTable for database representation.
""" 
class MeanMapper() :

    def to_api(self, mean: MeanTable) -> MeanModel :
        return MeanModel(
            id = mean.entity_id,
            name = mean.name,
            state = mean.state,
            location = mean.location,
            type= mean.type,
            classroom_id= mean.classroom.entity_id if mean.classroom else None,
            to_be_replaced= mean.to_be_replaced
        )
        
