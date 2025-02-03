from backend.domain.schemas.user import UserModel
from backend.domain.models.tables import UserTable

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