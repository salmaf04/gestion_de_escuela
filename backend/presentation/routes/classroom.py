from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.classroom import ClassroomCreateModel, ClassroomModel
from sqlalchemy.orm import Session
from backend.configuration import get_db
from backend.application.serializers.classroom import ClassroomMapper
from backend.application.services.classroom import ClassroomCreateService, ClassroomPaginationService, ClassroomDeletionService, ClassroomUpdateService
from backend.domain.filters.classroom import ClassroomFilterSchema, ClassroomChangeRequest

"""
This module defines API endpoints for managing classrooms using FastAPI.

Endpoints:
- POST /classroom: Create a new classroom.
- DELETE /classroom/{id}: Delete an existing classroom by its ID.
- GET /classroom: Retrieve a list of classrooms based on provided filters.
- PATCH /classroom/{id}: Update an existing classroom by its ID.

Dependencies:
- FastAPI's APIRouter for routing.
- SQLAlchemy's Session for database interactions.
- Custom services and models for handling classroom operations.

Functions:
- create_classroom: Handles the creation of a new classroom. Utilizes the ClassroomCreateService to add a classroom to the database.
- delete_classroom: Handles the deletion of a classroom. Validates the existence of the classroom and deletes it if valid.
- read_classroom: Retrieves a list of classrooms based on filter criteria. Utilizes the ClassroomPaginationService to fetch data.
- update_classroom: Updates an existing classroom. Validates the existence of the classroom and applies changes if valid.

Raises:
- HTTPException: Raised when a classroom is not found, with appropriate HTTP status codes.
"""

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
    classroom_service = ClassroomCreateService(session)
    classroom_pagination_service = ClassroomPaginationService(session)
    mapper = ClassroomMapper()
    
    check_classroom = classroom_pagination_service.get_classroom(
        filter_params=ClassroomFilterSchema(number=classroom_input.number)
    )

    if check_classroom :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="There is already a classroom with that number"
        )

    response = classroom_service.create_classroom(classroom=classroom_input)

    return mapper.to_api_default(response)

@router.delete(
    "/classroom/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_classroom(
    id: str,
    session: Session = Depends(get_db)
) :
    classroom_pagination_service = ClassroomPaginationService(session)
    classroom_deletion_service = ClassroomDeletionService(session)

    classroom =classroom_pagination_service.get_classroom_by_id(id=id)

    if not classroom :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no classroom with that id"
        )

    classroom_deletion_service.delete_classroom(classroom=classroom)

@router.get(
    "/classroom",
    response_model=list[ClassroomModel],
    status_code=status.HTTP_200_OK
)
async def read_classroom(
    filters: ClassroomFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    classroom_pagination_service = ClassroomPaginationService(session)
    mapper = ClassroomMapper()

    classrooms = classroom_pagination_service.get_classroom(filter_params=filters)
   
    if not classrooms :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no classroom with that id"
        )
         
    return mapper.to_api(classrooms)

@router.patch(
    "/classroom/{id}",
    response_model=ClassroomModel,
    status_code=status.HTTP_200_OK
)
async def update_classroom(
    id : str,
    filters: ClassroomChangeRequest,
    session: Session = Depends(get_db)
) :
    classroom_pagination_service = ClassroomPaginationService(session)
    classroom_update_service = ClassroomUpdateService(session)
    mapper = ClassroomMapper()

    classroom = classroom_pagination_service.get_classroom_by_id(id = id)
    classroom_model = mapper.to_api_default(classroom)

    if not classroom :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no classroom with that id"
        )
 
    classroom_updated = classroom_update_service.update_one(changes=filters, classroom=classroom_model)

    return classroom_updated
