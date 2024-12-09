from fastapi import APIRouter, status, Depends
from backend.domain.schemas.valoration import ValorationCreateModel, ValorationModel
from sqlalchemy.orm import Session
from backend.application.services.valoration import ValorationCreateService
from backend.application.serializers.valoration import ValorationMapper
from backend.configuration import get_db

router = APIRouter()

@router.post(
    "/valoration",
    response_model=ValorationModel,
    status_code=status.HTTP_201_CREATED
) 
async def create_valoration(
    valoration_input:ValorationCreateModel,
    session: Session = Depends(get_db)
) :
    valoration_service = ValorationCreateService()
    mapper = ValorationMapper()

    response = valoration_service.create_valoration(session=session, valoration=valoration_input)

    return mapper.to_api(response)