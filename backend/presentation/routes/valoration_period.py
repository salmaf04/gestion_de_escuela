from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.valoration_period import ValorationPeriodChangeRequest
from sqlalchemy.orm import Session
from backend.application.services.valoration_period import ValorationPeriodUpdateService
from backend.configuration import get_db

router = APIRouter()

@router.patch(
    "/valoration_period/",
    response_model=ValorationPeriodChangeRequest,
    status_code=status.HTTP_200_OK
)
async def update_valoration_period(
    valoration_period_input: ValorationPeriodChangeRequest,
    session: Session = Depends(get_db)
):
    valoration_period_service = ValorationPeriodUpdateService()

    valoration_period = valoration_period_service.update_one(session=session, changes=valoration_period_input)

    return valoration_period_input