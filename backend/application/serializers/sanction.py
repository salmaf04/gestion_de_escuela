from backend.domain.schemas.sanction import SanctionModel
from backend.domain.models.tables import SanctionTable


class SanctionMapper :
    def to_api(self, sanction: SanctionTable) -> SanctionModel :
        return SanctionModel(
            id = sanction.entity_id,
            amount=sanction.amount,
            teacher_id=sanction.teacher.id,
            date=sanction.date
        )