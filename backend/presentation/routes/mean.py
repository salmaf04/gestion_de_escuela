from backend.application.serializers.mean import MeanMapper
from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from fastapi import Depends, HTTPException, status
from backend.domain.schemas.mean import MeanModel, MeanCreateModel
from backend.application.services.mean import MeanCreateService, MeanPaginationService, MeanDeletionService, MeanUpdateService
from sqlalchemy.orm import Session
from backend.domain.filters.mean import MeanFilterSchema, ChangeRequest
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
    mean_service = MeanCreateService()
    mapper = MeanMapper()

    response = mean_service.mean_create(session=session, mean=model_input)

    return mapper.to_api(response)


@router.delete(
    "/mean/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_mean(
    id: str,
    session: Session = Depends(get_db)
) :
    mean_pagination_service = MeanPaginationService()
    mean_deletion_service = MeanDeletionService()

    mean =mean_pagination_service.get_mean_by_id(session=session, id=id)

    if not mean :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no mean with that id"
        )

    mean_deletion_service.delete_mean(session=session, mean=mean)


@router.get(
    "/mean",
    response_model=dict[int, MeanModel],
    status_code=status.HTTP_200_OK
)
async def read_mean(
    filters: MeanFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    mean_pagination_service = MeanPaginationService()
    mapper = MeanMapper()

    means = mean_pagination_service.get_means(session=session, filter_params=filters)

    if not means :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no means with that fields"
        )

    means_mapped = {}    
     
    for i, means in enumerate(means) :
        means_mapped[i] = mapper.to_api(means)
        
    return means_mapped
    
@router.patch(
    "/mean/{id}",
    response_model=MeanModel,
    status_code=status.HTTP_200_OK
)
async def mean_update(
    id : str,
    filters: ChangeRequest = Depends(),
    session: Session = Depends(get_db)
) :
    mean_pagination_service = MeanPaginationService()
    mean_update_service = MeanUpdateService()
    mapper = MeanMapper()

    mean = mean_pagination_service.get_mean_by_id(session=session, id = id)
    mean_model = mapper.to_api(mean)

    if not mean :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no mean with that id"
        )

    mean_updated = mean_update_service.update_one(session=session, changes=filters, mean=mean_model)

    return mean_updated

