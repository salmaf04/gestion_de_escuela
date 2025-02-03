from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.classroom_request import ClassroomRequestCreateModel, ClassroomRequestModel, ClassroomDeletionModel
from sqlalchemy.orm import Session
from backend.application.services.classroom import ClassroomPaginationService
from backend.application.services.classroom_request import ClassroomRequestCreateService, ClassroomRequestDeletionService, ClassroomRequestPaginationService
from fastapi.exceptions import HTTPException
from backend.application.serializers.classroom_request import ClassroomRequestMapper
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
    pagination_service = ClassroomPaginationService(session)
    create_service = ClassroomRequestCreateService(session)
    mapper = ClassroomRequestMapper()


    pagination_service.get_classroom_by_id(id=classroom.classroom_id)

    if not pagination_service :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no classroom with that id'
        )
    
    classroom_id = create_service.create_classroom_request(classroom_id=classroom.classroom_id,teacher_id=teacher_id)
    return mapper.to_api(teacher_id, classroom_id)
    

@router.delete(
    '/classroom_request/{teacher_id}',
    status_code=status.HTTP_200_OK
)
async def delete_mean_request(
    teacher_id: str,
    classroom : ClassroomDeletionModel,
    session : Session = Depends(get_db)
) :
    classroom_pagination = ClassroomRequestPaginationService(session)
    classroom_deletion = ClassroomRequestDeletionService(session)

    classroom_request = classroom_pagination.get_by_id(teacher_id=teacher_id,  classroom_id=classroom.classroom_id)

    if not classroom_request :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No existe solicitud de medio con esos datos"
        )
    
    classroom_deletion.delete(classroom_request=classroom_request)
    
        
