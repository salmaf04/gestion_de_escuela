from fastapi import APIRouter, HTTPException, status, Depends, Body
from backend.domain.schemas.mean_request import MeanRequestCreateModel, MeanRequestModel, MeanDeletionModel
from sqlalchemy.orm import Session
from backend.application.services.mean import MeanPaginationService
from backend.application.services.mean_request import MeanRequestCreateService, MeanRequestPaginationService, MeanRequestDeletionService
from fastapi.exceptions import HTTPException
from backend.application.serializers.mean_request import MeanRequestMapper
from backend.configuration import get_db


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
    
    


    

    

    

