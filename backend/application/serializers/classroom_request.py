from backend.domain.schemas.classroom_request import ClassroomRequestModel

"""
This module defines a mapper for converting classroom request data into API representations.

Classes:
    ClassroomRequestMapper: A utility class for mapping classroom request data to ClassroomRequestModel objects.

Class Details:

ClassroomRequestMapper:
    - This class provides a method to convert classroom request data, specifically teacher and classroom IDs, into a ClassroomRequestModel object, which is used in the API layer.
    
    Methods:
        - to_api(teacher_id, classroom_id) -> ClassroomRequestModel: 
            Converts the given teacher and classroom IDs into a ClassroomRequestModel object, mapping the relevant fields.

Dependencies:
    - ClassroomRequestModel for data representation.
"""
class ClassroomRequestMapper :
    def to_api(self,teacher_id, classroom_id) :
        return ClassroomRequestModel(
            teacher_id=teacher_id,
            classroom_id=classroom_id
        )
