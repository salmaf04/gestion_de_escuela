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

    def to_api(self, data) -> MeanModel :
        serialized_data = []
    
        for mean in data :
            serialized_data.append(MeanModel(
                id = mean[0].id,
                name = mean[0].name,
                state = mean[0].state,
                location = mean[0].location,
                type= mean[0].type,
                classroom_id= mean[0].classroom.entity_id if mean[0].classroom else None,
                to_be_replaced= mean[0].to_be_replaced,
                requested_by = str(mean[1]) if mean[1] else None
            ))

        return serialized_data
       
