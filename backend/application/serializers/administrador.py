from backend.domain.schemas.administrador import AdministratorModel 
from backend.domain.models.tables import AdministratorTable

"""
This module defines a mapper for converting between database and API representations of administrator records.

Classes:
    AdministratorMapper: A utility class for mapping AdministratorTable objects to AdministratorModel objects.

Class Details:

AdministratorMapper:
    - This class provides a method to convert an AdministratorTable object, which represents a database record, into an AdministratorModel object, which is used in the API layer.
    
    Methods:
        - to_api(administrator: AdministratorTable) -> AdministratorModel: 
            Converts the given AdministratorTable object into an AdministratorModel object, mapping the relevant fields.

Dependencies:
    - AdministratorModel and AdministratorTable for data representation.
"""

class AdministratorMapper:

    def to_api(self, administrator: AdministratorTable) -> AdministratorModel:
        return AdministratorModel(
            id=administrator.entity_id,
            name=administrator.name,
            lastname=administrator.lastname,
            username=administrator.username,
            email=administrator.email,
            hash_password=administrator.hashed_password   
        )