from fastapi import APIRouter, status, Depends, HTTPException
from backend.domain.schemas.valoration import ValorationCreateModel, ValorationModel, TeacherValoration
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
    valoration_service = ValorationCreateService(session)
    mapper = ValorationMapper()

    response = valoration_service.create_valoration(valoration=valoration_input)

    return mapper.to_api(response)

@router.get(
    "/valoration",
    response_model=dict[int, ValorationModel] | TeacherValoration | list,
    status_code=status.HTTP_200_OK
)
async def read_valoration(
    by_teacher_id : str = None,
    filters: ValorationFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    valoration_pagination_service = ValorationPaginationService(session)
    mapper = ValorationMapper()

    if by_teacher_id :
        valorations = valoration_pagination_service.get_valoration_by_teacher_id(teacher_id=by_teacher_id)
        valorations_mapped = mapper.to_valoration_by_subject(valorations)
        return valorations_mapped

    valorations = valoration_pagination_service.get_valoration(filter_params=filters)

    if not valorations :
        return []

    valorations_mapped = {}    
     
    for i, valoration in enumerate(valorations) :
        valorations_mapped[i] = mapper.to_api(valoration)
        
    return valorations_mapped