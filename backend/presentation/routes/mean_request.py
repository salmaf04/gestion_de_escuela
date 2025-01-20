from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.mean_request import MeanRequestCreateModel, MeanRequestModel
from sqlalchemy.orm import Session
from backend.application.services.mean import MeanPaginationService
from backend.application.services.mean_request import MeanRequestCreateService
from fastapi.exceptions import HTTPException
from backend.application.serializers.mean_request import MeanRequestMapper
from backend.domain.filters.administrador import ChangeRequest
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
    pagination_service = MeanPaginationService()
    create_service = MeanRequestCreateService()
    mapper = MeanRequestMapper()


    pagination_service.get_mean_by_id(session=session,id=mean.mean_id)

    if not pagination_service :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no mean with that id'
        )
    
    mean_id = create_service.create_mean_request(session=session,mean_id=mean.mean_id,teacher_id=teacher_id)
    return mapper.to_api(teacher_id, mean_id)
    

    

    

    

