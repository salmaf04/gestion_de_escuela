from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from backend.domain.schemas.sanction import SanctionCreateModel, SanctionModel
from backend.configuration import get_db
from sqlalchemy.orm import Session
from backend.application.services.sanction import SanctionCreateService
from backend.application.serializers.sanction import SanctionMapper

"""
This module defines an API endpoint for managing sanctions using FastAPI.

Endpoint:
- POST /sanction: Create a new sanction record.

Dependencies:
- FastAPI's APIRouter for routing.
- SQLAlchemy's Session for database interactions.
- Custom services and models for handling sanction operations.

Function:
- create_sanction: Handles the creation of a new sanction record. Utilizes the SanctionCreateService to add a sanction to the database.

Parameters:
- sanction_input (SanctionCreateModel): The data for creating a new sanction record.
- session (Session): The database session dependency.

Returns:
- JSON response with the created sanction record.

Raises:
- HTTPException: Can be raised if there are issues during the creation process, with appropriate HTTP status codes.
"""

router = APIRouter()

@router.post(
    "/sanction",
    response_model=SanctionModel,
    status_code=status.HTTP_201_CREATED
)
async def create_sanction(
    sanction_input: SanctionCreateModel,
    session: Session = Depends(get_db)
) :
    sanction_service = SanctionCreateService(session)
    mapper = SanctionMapper()
    sanction = sanction_service.create_sanction(sanction=sanction_input)
    return mapper.to_api(sanction)

    


