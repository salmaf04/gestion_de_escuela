from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.absence import AbsenceCreateModel, AbsenceModel
from sqlalchemy.orm import Session
from backend.application.services.absence import AbsenceCreateService
from fastapi.exceptions import HTTPException
from backend.application.serializers.absence import AbsenceMapper
from backend.configuration import get_db

router = APIRouter()

@router.post(
    "/absence",
    response_model=AbsenceModel,
    status_code=status.HTTP_201_CREATED
)
async def create_absence(
    absence_input: AbsenceCreateModel,
    session: Session = Depends(get_db)
) :
    absence_service = AbsenceCreateService()
    mapper = AbsenceMapper()

    response = absence_service.create_absence(session=session, absence=absence_input)

    return mapper.to_api(response)