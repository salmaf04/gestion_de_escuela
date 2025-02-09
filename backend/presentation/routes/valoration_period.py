from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.valoration_period import ValorationPeriodChangeRequest, ValorationPeriodModel
from sqlalchemy.orm import Session
from backend.application.services.valoration_period import ValorationPeriodUpdateService, ValorationPeriodPaginationService
from backend.configuration import get_db
from backend.application.serializers.valoration_period import ValorationPeriodMapper

"""
This module defines an API endpoint for updating valoration periods using FastAPI.

Endpoint:
- PATCH /valoration_period/: Update an existing valoration period.

Dependencies:
- FastAPI's APIRouter for routing.
- SQLAlchemy's Session for database interactions.
- Custom services for handling valoration period operations.

Function:
- update_valoration_period: Handles the update of an existing valoration period. Utilizes the ValorationPeriodUpdateService to apply changes to the valoration period.

Parameters:
- valoration_period_input (ValorationPeriodChangeRequest): The changes to apply to the valoration period.
- session (Session): The database session dependency.

Returns:
- The updated valoration period input as a JSON response.

Raises:
- HTTPException: Can be raised if there are issues during the update process, with appropriate HTTP status codes.
"""

router = APIRouter()

@router.patch(
    "/valoration_period",
    response_model=ValorationPeriodChangeRequest,
    status_code=status.HTTP_200_OK
)
async def update_valoration_period(
    valoration_period_input: ValorationPeriodChangeRequest,
    session: Session = Depends(get_db)
):
    valoration_period_service = ValorationPeriodUpdateService(session)

    valoration_period = valoration_period_service.update_one(changes=valoration_period_input)

    return valoration_period_input

@router.get(
    "/valoration_period",
    response_model=ValorationPeriodModel,
    status_code=status.HTTP_200_OK
)
async def get_valoration_period(
    session: Session = Depends(get_db)
):
    valoration_period_service = ValorationPeriodPaginationService(session)
    mapper = ValorationPeriodMapper()

    valoration_period = valoration_period_service.get_valoration_period(filter_params=None)

    return mapper.to_api(valoration_period)