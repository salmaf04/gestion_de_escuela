from backend.domain.schemas.mean_request import MeanRequestModel

"""
This module defines a mapper for converting mean request data into API representations.

Classes:
    MeanRequestMapper: A utility class for mapping mean request data to MeanRequestModel objects.

Class Details:

MeanRequestMapper:
    - This class provides a method to convert mean request data, specifically teacher and mean IDs, into a MeanRequestModel object, which is used in the API layer.
    
    Methods:
        - to_api(teacher_id, mean_id) -> MeanRequestModel: 
            Converts the given teacher and mean IDs into a MeanRequestModel object, mapping the relevant fields.

Dependencies:
    - MeanRequestModel for API data representation.
"""

class MeanRequestMapper :
    def to_api(self,teacher_id, mean_id) :
        return MeanRequestModel(
            teacher_id=teacher_id,
            mean_id=mean_id
        )
