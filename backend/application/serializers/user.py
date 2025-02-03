from backend.domain.schemas.user import UserModel
from backend.domain.models.tables import UserTable

"""
This module defines a mapper for converting user data into API representations.

Classes:
    UserMapper: A utility class for mapping UserTable objects to UserModel objects.

Class Details:

UserMapper:
    - This class provides a method to convert a UserTable object, which represents a database record, into a UserModel object, which is used in the API layer.
    
    Methods:
        - to_api(user: UserTable) -> UserModel: 
            Converts the given UserTable object into a UserModel object, mapping the relevant fields such as ID, name, lastname, email, username, hashed password, type, and roles.

Dependencies:
    - UserModel for API data representation.
    - UserTable for database representation.
"""
class UserMapper() :

    def to_api(self, user: UserTable) -> UserModel :
        return UserModel(
            id=user.entity_id,
            name=user.name,
            lastname=user.lastname,
            email=user.email,
            username=user.username,
            hashed_password=user.hashed_password,
            type=user.type,
            roles=user.roles
        )