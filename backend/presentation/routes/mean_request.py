from fastapi import APIRouter, HTTPException, status, Depends, Body
from backend.domain.schemas.mean_request import MeanRequestCreateModel, MeanRequestModel, MeanDeletionModel
from sqlalchemy.orm import Session
from backend.application.services.mean import MeanPaginationService
from backend.application.services.mean_request import MeanRequestCreateService, MeanRequestPaginationService, MeanRequestDeletionService
from fastapi.exceptions import HTTPException
from backend.application.serializers.mean_request import MeanRequestMapper
from backend.configuration import get_db

"""
This module defines API endpoints for managing mean requests using FastAPI.

Endpoints:
- POST /mean_request/{teacher_id}: Create a new mean request for a specific teacher.
- DELETE /mean_request/{teacher_id}: Delete an existing mean request for a specific teacher.

Dependencies:
- FastAPI's APIRouter for routing.
- SQLAlchemy's Session for database interactions.
- Custom services and models for handling mean request operations.

Functions:
- create_mean_request: Handles the creation of a mean request. Validates the existence of the mean and creates a request if valid.
- delete_mean_request: Handles the deletion of a mean request. Validates the existence of the request and deletes it if valid.

Parameters:
- teacher_id (str): The ID of the teacher for whom the mean request is being created or deleted.
- mean (MeanRequestCreateModel or MeanDeletionModel): The data for creating or deleting a mean request.
- session (Session): The database session dependency.

Returns:
- JSON response with the created mean request or confirmation of deletion.

Raises:
- HTTPException: Raised when a mean or request is not found, with appropriate HTTP status codes.
"""

router = APIRouter()

@router.post(
    '/mean_request/{teacher_id}',
    response_model=MeanRequestModel,
    status_code=status.HTTP_201_CREATED
)
async def create_mean_request(
    teacher_id : str,
    mean : MeanRequestCreateModel,
    session: Session = Depends(get_db)
) :
    pagination_service = MeanPaginationService(session)
    create_service = MeanRequestCreateService(session)
    mapper = MeanRequestMapper()


    pagination_service.get_mean_by_id(id=mean.mean_id)

    if not pagination_service :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no mean with that id'
        )
    
    mean_id = create_service.create_mean_request(mean_id=mean.mean_id,teacher_id=teacher_id)
    return mapper.to_api(teacher_id, mean_id)

@router.delete(
    '/mean_request/{teacher_id}',
    status_code=status.HTTP_200_OK
)
async def delete_mean_request(
    teacher_id: str,
    mean : MeanDeletionModel,
    session : Session = Depends(get_db)
) :
    mean_request_pagination = MeanRequestPaginationService(session)
    mean_request_deletion = MeanRequestDeletionService(session)

    mean_request = mean_request_pagination.get_by_id(teacher_id=teacher_id, mean_id=mean.mean_id)

    if not mean_request :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No existe solicitud de medio con esos datos"
        )
    
    mean_request_deletion.delete(mean_request=mean_request)
    
    


    

    

    

