from fastapi import APIRouter, status, Depends, HTTPException
from backend.domain.schemas.valoration import ValorationCreateModel, ValorationModel
from sqlalchemy.orm import Session
from backend.application.services.valoration import ValorationCreateService, ValorationPaginationService
from backend.application.serializers.valoration import ValorationMapper
from backend.configuration import get_db
from backend.domain.filters.valoration import ValorationFilterSchema

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

@router.get(
    "/valoration",
    response_model=dict[int, ValorationModel],
    status_code=status.HTTP_200_OK
)
async def read_valoration(
    filters: ValorationFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    valoration_pagination_service = ValorationPaginationService()
    mapper = ValorationMapper()

    valorations = valoration_pagination_service.get_valoration(session=session, filter_params=filters)

    if not valorations :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no valoration with that fields"
        )

    valorations_mapped = {}    
     
    for i, valoration in enumerate(valorations) :
        valorations_mapped[i] = mapper.to_api(valoration)
        
    return valorations_mapped