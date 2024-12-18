from backend.domain.schemas.administrador import AdministratorModel 
from backend.domain.models.tables import AdministratorTable

class AdministratorMapper:

    def to_api(self, administrator: AdministratorTable) -> AdministratorModel:
        return AdministratorModel(
            id=administrator.entity_id,
            name=administrator.name,
            username=administrator.username,
            email=administrator.email,
            hash_password=administrator.hash_password   
        )