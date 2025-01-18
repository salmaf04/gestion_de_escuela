from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.classroom_request import ClassroomRequestCreateModel, ClassroomRequestModel
from sqlalchemy.orm import Session
from backend.application.services.classroom import ClassroomPaginationService
from backend.application.services.classroom_request import ClassroomRequestCreateService
from fastapi.exceptions import HTTPException
from backend.application.serializers.classroom_request import ClassroomRequestMapper
from backend.domain.filters.administrador import ChangeRequest
from backend.configuration import get_db


router = APIRouter()

@router.post(
    '/classroom_request/{teacher_id}',
    response_model=ClassroomRequestModel,
    status_code=status.HTTP_201_CREATED
)
async def create_mean_request(
    teacher_id : str,
    classroom : ClassroomRequestCreateModel,
    session: Session = Depends(get_db)
) :
    pagination_service = ClassroomPaginationService()
    create_service = ClassroomRequestCreateService()
    mapper = ClassroomRequestMapper()


    pagination_service.get_classroom_by_id(session=session,id=classroom.classroom_id)

    if not pagination_service :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no classroom with that id'
        )
    
    classroom_id = create_service.create_classroom_request(session=session,classroom_id=classroom.classroom_id,teacher_id=teacher_id)
    return mapper.to_api(teacher_id, classroom_id)
    

    
