from fastapi import APIRouter, status, Depends, HTTPException
from backend.domain.schemas.valoration import ValorationCreateModel, ValorationModel, TeacherValoration
from sqlalchemy.orm import Session
from backend.application.services.valoration import ValorationCreateService, ValorationPaginationService
from backend.application.serializers.valoration import ValorationMapper
from backend.configuration import get_db
from backend.domain.filters.valoration import ValorationFilterSchema

"""
This module defines API endpoints for managing valorations using FastAPI.

Endpoints:
- POST /valoration: Create a new valoration. Ensures that a student cannot rate the same teacher more than once.
- GET /valoration: Retrieve a list of valorations based on provided filters, including options for valorations by teacher ID.

Dependencies:
- FastAPI's APIRouter for routing.
- SQLAlchemy's Session for database interactions.
- Custom services and models for handling valoration operations.

Functions:
- create_valoration: Handles the creation of a new valoration. Validates that a student has not already rated the same teacher.
- read_valoration: Retrieves valorations based on filter criteria, including options for valorations by teacher ID.

Parameters:
- valoration_input (ValorationCreateModel): The data for creating a new valoration.
- by_teacher_id (str): The ID of the teacher to filter valorations by.
- filters (ValorationFilterSchema): The filter criteria for retrieving valorations.
- session (Session): The database session dependency.

Returns:
- JSON responses with the created or retrieved valoration records.

Raises:
- HTTPException: Raised when a valoration is not found or when attempting to create a duplicate, with appropriate HTTP status codes.
"""

router = APIRouter()

@router.post(
    "/valoration",
    response_model=ValorationModel,
    status_code=status.HTTP_201_CREATED
) 
async def create_valoration(
    valoration_input:ValorationCreateModel,
    session: Session = Depends(get_db)
) :
    valoration_service = ValorationCreateService(session)
    valoration_pagination_service = ValorationPaginationService(session)
    mapper = ValorationMapper()

    valoration_filter_by_student_id = ValorationFilterSchema(student_id=valoration_input.student_id, teacher_id=valoration_input.teacher_id)
    
    response = valoration_service.create_valoration(valoration=valoration_input)

    return mapper.to_api(response)

@router.get(
    "/valoration",
    response_model=dict[int, ValorationModel] | list[ValorationModel] | list,
    status_code=status.HTTP_200_OK
)
async def read_valoration(
    by_teacher_id : str = None,
    filters: ValorationFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    valoration_pagination_service = ValorationPaginationService(session)
    mapper = ValorationMapper()

    if by_teacher_id :
        valorations = valoration_pagination_service.get_valoration_by_teacher_id(teacher_id=by_teacher_id)
        valorations_mapped = mapper.to_valoration_by_subject(valorations)
        return valorations_mapped

    valorations = valoration_pagination_service.get_valoration(filter_params=filters)

    if not valorations :
        return []

    valorations_mapped = []
     
    for valoration in valorations :
        valorations_mapped.append(mapper.to_api(valoration))
        
    return valorations_mapped