from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from backend.domain.schemas.secretary import SecretaryModel, SecretaryCreateModel
from sqlalchemy.orm import Session
from backend.application.services.secretary import SecretaryCreateService, SecretaryPaginationService, SecretaryDeletionService, SecretaryUpdateService
from fastapi.exceptions import HTTPException
from backend.application.serializers.secretary import SecretaryMapper
from backend.domain.filters.secretary import SecretaryChangeRequest, SecretaryFilterSchema
from backend.configuration import get_db

"""
This module defines API endpoints for managing secretaries using FastAPI.

Endpoints:
- POST /secretary: Create a new secretary. Ensures no duplicate email addresses.
- DELETE /secretary/{id}: Delete an existing secretary by their ID.
- PATCH /secretary/{id}: Update an existing secretary by their ID.
- GET /secretary: Retrieve a list of secretaries based on provided filters.

Dependencies:
- FastAPI's APIRouter for routing.
- SQLAlchemy's Session for database interactions.
- Custom services and models for handling secretary operations.

Functions:
- create_secretary: Handles the creation of a new secretary. Validates that no secretary with the same email exists.
- delete_secretary: Handles the deletion of a secretary. Validates the existence of the secretary and deletes them if valid.
- update_secretary: Updates an existing secretary. Validates the existence of the secretary and applies changes if valid.
- read_secretary: Retrieves a list of secretaries based on filter criteria. Utilizes the SecretaryPaginationService to fetch data.

Parameters:
- secretary_input (SecretaryCreateModel): The data for creating a new secretary.
- id (str): The ID of the secretary to delete or update.
- filters (SecretaryFilterSchema): The filter criteria for retrieving secretaries.
- session (Session): The database session dependency.

Returns:
- JSON responses with the created, retrieved, or updated secretary records.

Raises:
- HTTPException: Raised when a secretary is not found or when attempting to create a duplicate, with appropriate HTTP status codes.
"""

router = APIRouter()


@router.post(
    "/secretary",
    response_model= SecretaryModel,
    status_code=status.HTTP_201_CREATED
)
async def create_secretary(
    secretary_input: SecretaryCreateModel,
    session: Session = Depends(get_db)
) :
    secretary_service = SecretaryCreateService(session)
    secretary_pagination_service = SecretaryPaginationService(session)
    mapper = SecretaryMapper()

    secretary = secretary_pagination_service.get_secretary_by_email(email=secretary_input.email)

    if secretary :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="There is already an secretary with that email"
        )

    response = secretary_service.create_secretary(secretary=secretary_input)

    return mapper.to_api(response)

@router.delete(
    "/secretary/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_secretary(
    id: str,
    session: Session = Depends(get_db)
) :
    secretary_pagination_service = SecretaryPaginationService(session)
    secretary_deletion_service = SecretaryDeletionService(session)

    secretary =secretary_pagination_service.get_secretary_by_id(id=id)

    if not secretary :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no secretary with that email"
        )

    secretary_deletion_service.delete_secretary(secretary=secretary)
    
@router.patch(
    "/secretary/{id}",
    response_model=SecretaryModel,
    status_code=status.HTTP_200_OK
)
async def update_secretary(
    id : str,
    filters: SecretaryChangeRequest,
    session: Session = Depends(get_db)
) :
    secretary_pagination_service = SecretaryPaginationService(session)
    secretary_update_service = SecretaryUpdateService(session)
    mapper = SecretaryMapper()

    secretary = secretary_pagination_service.get_secretary_by_id(id = id)
    secretary_model = mapper.to_api(secretary)

    if not secretary :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no secretary with that id"
        )
    
    secretary_updated = secretary_update_service.update_one(changes=filters, secretary=secretary_model)

    return secretary_updated

    
@router.get(
    "/secretary",
    response_model=list[SecretaryModel] | SecretaryModel,
    status_code=status.HTTP_200_OK
)
async def read_secretary(
    filters: SecretaryFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    secretary_pagination_service = SecretaryPaginationService(session)

    secretary = secretary_pagination_service.get(filter_params=filters)

    if not secretary :
        return []
    
    secretary_mapped = []

    for secretary in secretary :
        secretary_mapped.append(SecretaryMapper().to_api(secretary))
        
    return secretary_mapped
