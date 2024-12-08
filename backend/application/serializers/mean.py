from backend.domain.schemas.mean import MeanModel
from database.tables import MeanTable

class MeanMapper() :

    def to_api(self, mean: MeanTable) -> MeanModel :
        return MeanModel(
            id = mean.entity_id,
            name = mean.name,
            state = mean.state,
            location = mean.location
        )
        
