from .schemas import SecretaryModel
from database.tables import SecretaryTable

class SecretaryMapper :

    def to_api(self, secretary: SecretaryTable) -> SecretaryModel :
        return SecretaryModel(
            id = secretary.entity_id,
            name= secretary.name,
            username= secretary.username,
            email= secretary.email,
            hash_password= secretary.hash_password,
        )