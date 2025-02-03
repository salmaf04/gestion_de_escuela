from backend.domain.schemas.mean import MeanModel
from backend.domain.models.tables import MeanTable

class MeanMapper() :

    def to_api(self, mean: MeanTable) -> MeanModel :
        return MeanModel(
            id = mean.entity_id,
            name = mean.name,
            state = mean.state,
            location = mean.location,
            type= mean.type,
            classroom_id= mean.classroom.entity_id if mean.classroom else None
        )
        
