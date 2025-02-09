from backend.domain.schemas.valoration_period import ValorationPeriodModel

class ValorationPeriodMapper :
    def to_api(self, data) -> ValorationPeriodModel :
        return ValorationPeriodModel(
            open = data.open
        )