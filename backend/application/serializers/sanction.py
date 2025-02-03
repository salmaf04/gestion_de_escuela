from backend.domain.schemas.sanction import SanctionModel
from backend.domain.models.tables import SanctionTable

"""
This module defines a mapper for converting sanction data into API representations.

Classes:
    SanctionMapper: A utility class for mapping SanctionTable objects to SanctionModel objects.

Class Details:

SanctionMapper:
    - This class provides a method to convert a SanctionTable object, which represents a database record, into a SanctionModel object, which is used in the API layer.
    
    Methods:
        - to_api(sanction: SanctionTable) -> SanctionModel: 
            Converts the given SanctionTable object into a SanctionModel object, mapping the relevant fields such as ID, amount, teacher ID, and date.

Dependencies:
    - SanctionModel for API data representation.
    - SanctionTable for database representation.
"""

class SanctionMapper :
    def to_api(self, sanction: SanctionTable) -> SanctionModel :
        return SanctionModel(
            id = sanction.entity_id,
            amount=sanction.amount,
            teacher_id=sanction.teacher.id,
            date=sanction.date
        )