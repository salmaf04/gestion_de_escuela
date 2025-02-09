from backend.application.serializers.mean import MeanMapper
from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from fastapi import Depends, HTTPException, status
from backend.domain.schemas.mean import MeanModel, MeanCreateModel
from backend.application.services.mean import MeanCreateService, MeanPaginationService, MeanDeletionService, MeanUpdateService
from sqlalchemy.orm import Session
from backend.domain.filters.mean import MeanFilterSchema, MeanChangeRequest
from backend.configuration import get_db

"""
This module defines API endpoints for managing means using FastAPI.

Endpoints:
- POST /mean: Create a new mean.
- DELETE /mean/{id}: Delete an existing mean by its ID.
- GET /mean: Retrieve a list of means based on provided filters or available means.
- PATCH /mean/{id}: Update an existing mean by its ID.

Dependencies:
- FastAPI's APIRouter for routing.
- SQLAlchemy's Session for database interactions.
- Custom services and models for handling mean operations.

Functions:
- create_mean: Handles the creation of a new mean. Utilizes the MeanCreateService to add a mean to the database.
- delete_mean: Handles the deletion of a mean. Validates the existence of the mean and deletes it if valid.
- read_mean: Retrieves a list of means based on filter criteria or available means. Utilizes the MeanPaginationService to fetch data.
- mean_update: Updates an existing mean. Validates the existence of the mean and applies changes if valid.

Parameters:
- model_input (MeanCreateModel): The data for creating a new mean.
- id (str): The ID of the mean to delete or update.
- filters (MeanFilterSchema): The filter criteria for retrieving means.
- avaliable_means (bool): Indicates if the user wants to retrieve only available means.
- filters (MeanChangeRequest): The changes to apply to the mean.

Returns:
- JSON responses with the created, retrieved, or updated mean records.

Raises:
- HTTPException: Raised when a mean is not found, with appropriate HTTP status codes.
"""

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
    mean_service = MeanCreateService(session)
    mapper = MeanMapper()

    response = mean_service.mean_create(mean=model_input)

    return mapper.to_api_default(response)


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
    response_model=list[MeanModel] | MeanModel| list,
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

    return mapper.to_api(means)
    
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
    mean_model = mapper.to_api_default(mean)

    if not mean :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no mean with that id"
        )

    mean_updated = mean_update_service.update_one(changes=filters, mean=mean_model)

    return mean_updated

