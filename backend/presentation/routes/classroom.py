from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.classroom import ClassroomCreateModel, ClassroomModel
from sqlalchemy.orm import Session
from backend.configuration import get_db
from backend.application.serializers.classroom import ClassroomMapper
from backend.application.services.classroom import ClassroomCreateService

router = APIRouter()

@router.post(
    "/classroom",
    response_model= ClassroomCreateModel,
    status_code=status.HTTP_201_CREATED
)
async def create_classroom(
    classroom_input: ClassroomCreateModel ,
    session: Session = Depends(get_db)
) :
    classroom_service = ClassroomCreateService()
    mapper = ClassroomMapper()

    response = classroom_service.create_classroom(session=session, classroom=classroom_input)

    return mapper.to_api(response)
