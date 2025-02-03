from backend.application.serializers.mean import MeanMapper
from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from fastapi import Depends, HTTPException, status
from backend.domain.schemas.mean import MeanModel, MeanCreateModel
from backend.application.services.mean import MeanCreateService, MeanPaginationService, MeanDeletionService, MeanUpdateService
from sqlalchemy.orm import Session
from backend.domain.filters.mean import MeanFilterSchema, MeanChangeRequest
from backend.configuration import get_db


router = APIRouter()


@router.post(
    "/mean",
    response_model=MeanModel,
    status_code=status.HTTP_201_CREATED
)
async def create_mean(
    model_input: MeanCreateModel,
    session: Session = Depends(get_db)
) :
    print(model_input)
    mean_service = MeanCreateService(session)
    mapper = MeanMapper()

    response = mean_service.mean_create(mean=model_input)

    return mapper.to_api(response)


@router.delete(
    "/mean/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_mean(
    id: str,
    session: Session = Depends(get_db)
) :
    mean_pagination_service = MeanPaginationService(session)
    mean_deletion_service = MeanDeletionService(session)

    mean =mean_pagination_service.get_mean_by_id(id=id)

    if not mean :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no mean with that id"
        )

    mean_deletion_service.delete_mean(mean=mean)


@router.get(
    "/mean",
    response_model=list[MeanModel] | MeanModel,
    status_code=status.HTTP_200_OK
)
async def read_mean(
    avaliable_means: bool = False,
    filters: MeanFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    mean_pagination_service = MeanPaginationService(session)
    mapper = MeanMapper()

    if avaliable_means :
        means = mean_pagination_service.get_avaliable_means()
    else :
        means = mean_pagination_service.get_means(filter_params=filters)

    means_mapped = [mapper.to_api(mean) for mean in means] if means else []
        
    return means_mapped
    
@router.patch(
    "/mean/{id}",
    response_model=MeanModel,
    status_code=status.HTTP_200_OK
)
async def mean_update(
    id : str,
    filters: MeanChangeRequest,
    session: Session = Depends(get_db)
) :
    mean_pagination_service = MeanPaginationService(session)
    mean_update_service = MeanUpdateService(session)
    mapper = MeanMapper()

    mean = mean_pagination_service.get_mean_by_id(id = id)
    mean_model = mapper.to_api(mean)

    if not mean :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no mean with that id"
        )

    mean_updated = mean_update_service.update_one(changes=filters, mean=mean_model)

    return mean_updated

