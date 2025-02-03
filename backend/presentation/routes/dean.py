from fastapi import HTTPException, status, Depends, APIRouter
from backend.domain.schemas.dean import DeanCreateModel, DeanModel
from sqlalchemy.orm import Session
from backend.application.services.dean import DeanCreateService, DeanPaginationService, DeanDeletionService, DeanUpdateService
from fastapi.exceptions import HTTPException
from backend.application.serializers.dean import DeanMapper
from backend.domain.filters.dean import DeanFilterSchema, DeanChangeRequest
from backend.configuration import get_db


router = APIRouter()


@router.post(
    "/dean",
    response_model=DeanModel,
    status_code=status.HTTP_201_CREATED
)
async def create_dean(
    dean_input: DeanCreateModel,
    session: Session = Depends(get_db)
) :
    dean_service = DeanCreateService(session)
    dean_pagination_service = DeanPaginationService(session)
    mapper = DeanMapper()

    dean = dean_pagination_service.get_dean(DeanFilterSchema())

    if dean :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Ya existe un decano"
        )

    response = dean_service.create_dean(dean=dean_input)

    return mapper.to_api(response)

@router.delete(
    "/dean/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_dean(
    id: str,
    session: Session = Depends(get_db)
) :
    dean_pagination_service = DeanPaginationService(session)
    dean_deletion_service = DeanDeletionService(session)

    dean =dean_pagination_service.get_dean_by_id(id=id)

    if not dean :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no dean with that email"
        )

    dean_deletion_service.delete_dean(dean=dean)
    
@router.get(
    "/dean",
    response_model=dict[int, DeanModel],
    status_code=status.HTTP_200_OK
)
async def read_dean(
    filters: DeanFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    dean_pagination_service = DeanPaginationService(session)
    mapper = DeanMapper()

    deans = dean_pagination_service.get_dean(filter_params=filters)

    if not deans :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no dean with that email"
        )

    deans_mapped = {}    
  
    for i, dean in enumerate(deans) :
        deans_mapped[i] = mapper.to_api(dean)
        
    return deans_mapped

@router.patch(
    "/dean/{id}",
    response_model=DeanModel,
    status_code=status.HTTP_200_OK
)
async def update_dean(
    id : str,
    filters: DeanChangeRequest,
    session: Session = Depends(get_db)
) :
    dean_pagination_service = DeanPaginationService(session)
    dean_update_service = DeanUpdateService(session)
    mapper = DeanMapper()

    dean = dean_pagination_service.get_dean_by_id(id = id)
    dean_model = mapper.to_api(dean)

    if not dean :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no dean with that id"
        )
    
    dean_updated = dean_update_service.update_one(changes=filters, dean=dean_model)

    return dean_updated