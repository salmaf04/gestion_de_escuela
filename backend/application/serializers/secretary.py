from backend.domain.schemas.secretary import SecretaryModel
from backend.domain.models.tables import SecretaryTable

"""
This module defines a mapper for converting secretary data into API representations.

Classes:
    SecretaryMapper: A utility class for mapping SecretaryTable objects to SecretaryModel objects.

Class Details:

SecretaryMapper:
    - This class provides a method to convert a SecretaryTable object, which represents a database record, into a SecretaryModel object, which is used in the API layer.
    
    Methods:
        - to_api(secretary: SecretaryTable) -> SecretaryModel: 
            Converts the given SecretaryTable object into a SecretaryModel object, mapping the relevant fields such as ID, name, lastname, username, email, and hashed password.

Dependencies:
    - SecretaryModel for API data representation.
    - SecretaryTable for database representation.
"""

class SecretaryMapper :

    def to_api(self, secretary: SecretaryTable) -> SecretaryModel :
        return SecretaryModel(
            id = secretary.entity_id,
            name= secretary.name,
            lastname= secretary.lastname,
            username= secretary.username,
            email= secretary.email,
            hash_password= secretary.hashed_password,
        )

