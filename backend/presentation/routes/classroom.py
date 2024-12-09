from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.classroom import ClassroomCreateModel, ClassroomModel
from sqlalchemy.orm import Session
from backend.configuration import get_db
from backend.application.serializers.classroom import ClassroomMapper
from backend.application.services.classroom import ClassroomCreateService, ClassroomPaginationService, ClassroomDeletionService, ClassroomUpdateService
from backend.domain.filters.classroom import ClassroomFilterSchema, ChangeRequest

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

@router.delete(
    "/classroom/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_classroom(
    id: str,
    session: Session = Depends(get_db)
) :
    classroom_pagination_service = ClassroomPaginationService()
    classroom_deletion_service = ClassroomDeletionService()

    classroom =classroom_pagination_service.get_classroom_by_id(session=session, id=id)

    if not classroom :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no classroom with that id"
        )

    classroom_deletion_service.delete_classroom(session=session, classroom=classroom)

@router.get(
    "/classroom",
    response_model=dict[int, ClassroomModel],
    status_code=status.HTTP_200_OK
)
async def read_classroom(
    filters: ClassroomFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    classroom_pagination_service = ClassroomPaginationService()
    mapper = ClassroomMapper()

    classrooms = classroom_pagination_service.get_classrooms(session=session, filter_params=filters)

    if not classrooms :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no classroom with that id"
        )

    classrooms_mapped = {}    
     
    for i, classroom in enumerate(classrooms) :
        classrooms_mapped[i] = mapper.to_api(classroom)
        
    return classrooms_mapped

@router.patch(
    "/classroom/{id}",
    response_model=ClassroomModel,
    status_code=status.HTTP_200_OK
)
async def update_classroom(
    id : str,
    filters: ChangeRequest = Depends(),
    session: Session = Depends(get_db)
) :
    classroom_pagination_service = ClassroomPaginationService()
    classroom_update_service = ClassroomUpdateService()
    mapper = ClassroomMapper()

    classroom = classroom_pagination_service.get_classroom_by_id(session=session, id = id)
    classroom_model = mapper.to_api(classroom)

    if not classroom :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no classroom with that id"
        )
    print(filters.specialty)

    classroom_updated = classroom_update_service.update_one(session=session, changes=filters, classroom=classroom_model)

    return classroom_updated
