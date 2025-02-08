from backend.domain.schemas.dean import DeanModel
from backend.domain.models.tables import DeanTable

"""
This module defines a mapper for converting dean data into API representations.

Classes:
    DeanMapper: A utility class for mapping DeanTable objects to DeanModel objects.

Class Details:

DeanMapper:
    - This class provides a method to convert a DeanTable object, which represents a database record, into a DeanModel object, which is used in the API layer.
    
    Methods:
        - to_api(dean: DeanTable) -> DeanModel: 
            Converts the given DeanTable object into a DeanModel object, mapping the relevant fields such as ID, name, lastname, email, specialty, contract type, experience, and username.

Dependencies:
    - DeanModel for API data representation.
    - DeanTable for database representation.
"""

class DeanMapper :

    def to_api(self, dean: DeanTable) -> DeanModel :
        return DeanModel(
            id = dean.entity_id,
            name=dean.name,
            lastname=dean.lastname,
            email=dean.email,
            specialty=dean.specialty,
            contract_type=dean.contract_type,
            salary=dean.salary,
            experience=dean.experience,
            username=dean.username,
        )