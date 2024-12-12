from backend.domain.schemas.dean import DeanModel
from backend.domain.models.tables import DeanTable

class DeanMapper :

    def to_api(self, dean: DeanTable) -> DeanModel :
        return DeanModel(
            id = dean.entity_id,
            name=dean.name,
            fullname=dean.fullname,
            email=dean.email,
            specialty=dean.specialty,
            contract_type=dean.contract_type,
            experience=dean.experience,
            username=dean.username,
        )