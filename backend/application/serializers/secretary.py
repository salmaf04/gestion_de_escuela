from backend.domain.schemas.secretary import SecretaryModel
from backend.domain.models.tables import SecretaryTable

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

