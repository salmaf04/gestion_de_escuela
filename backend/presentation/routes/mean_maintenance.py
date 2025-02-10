from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.mean_maintenance import MeanMaintenanceCreateModel, MeanMaintenanceModel
from sqlalchemy.orm import Session
from backend.application.services.mean_maintenance import MeanMaintenanceCreateService, MeanMaintenancePaginationService, MeanMaintenanceUpdateService, MeanMaintenanceDeleteService
from backend.application.serializers.mean_maintenance import MeanMaintenanceMapper, MeanMaintenanceDate
from backend.configuration import get_db
from backend.domain.filters.mean_maintenance import MeanMaintenanceFilterSchema, MeanMaintenanceChangeRequest
from typing import Annotated
from fastapi import Query
from fastapi.encoders import jsonable_encoder
from typing import List, Any
from backend.presentation.utils.auth import authorize
from fastapi import Request
from backend.domain.schemas.user import UserModel
from backend.presentation.utils.auth import get_current_user

"""
This module defines API endpoints for managing mean maintenance records using FastAPI.

Endpoints:
- POST /mean_maintenance: Create a new mean maintenance record.
- GET /mean_maintenance: Retrieve mean maintenance records based on filters, including options for maintenance by classroom or date.
- PATCH /mean_maintenance/{id}: Update an existing mean maintenance record by its ID.

Dependencies:
- FastAPI's APIRouter for routing.
- SQLAlchemy's Session for database interactions.
- Custom services and models for handling mean maintenance operations.

Functions:
- create_mean_maintenance: Handles the creation of a new mean maintenance record. Utilizes the MeanMaintenanceCreateService to add a record to the database.
- read_mean_maintenance: Retrieves mean maintenance records based on filter criteria. Supports filtering by classroom or date.
- update_teacher: Updates an existing mean maintenance record. Validates the existence of the record and applies changes if valid. Requires administrator authorization.

Parameters:
- mean_maintenance_input (MeanMaintenanceCreateModel): The data for creating a new mean maintenance record.
- filters (MeanMaintenanceFilterSchema): The filter criteria for retrieving mean maintenance records.
- mainteniance_by_classroom_filter (bool): Indicates if the user wants to filter maintenance by classroom.
- date_filter (bool): Indicates if the user wants to filter maintenance by date.
- id (str): The ID of the mean maintenance record to update.
- filters (MeanMaintenanceChangeRequest): The changes to apply to the mean maintenance record.

Returns:
- JSON responses with the created, retrieved, or updated mean maintenance records.

Raises:
- HTTPException: Raised when a mean maintenance record is not found, with appropriate HTTP status codes.
"""

router = APIRouter()

@router.post(
    "/mean_maintenance",
    response_model=MeanMaintenanceModel,
    status_code=status.HTTP_201_CREATED
)
async def create_mean_maintenance(
    mean_maintenance_input: MeanMaintenanceCreateModel,
    session: Session = Depends(get_db)
) :
    mean_maintenance_service = MeanMaintenanceCreateService(session)
    mapper = MeanMaintenanceMapper()

    response = mean_maintenance_service.create_mean_maintenance(mean_maintenance=mean_maintenance_input)

    return mapper.to_api(response)


@router.get(
    "/mean_maintenance",
    response_model=dict[int, MeanMaintenanceModel] | List[Any] | int,
    status_code=status.HTTP_200_OK
)
async def read_mean_maintenance(
    date_filter = False,
    filters: MeanMaintenanceFilterSchema = Depends(),
    session: Session = Depends(get_db),
    mainteniance_by_classroom_filter : Annotated[
        bool,
        Query(
            description="Indicates if the user wants to access the maintenance by classroom filter",
        ),
    ] = False  
) :
    mean_maintenance_pagination_service = MeanMaintenancePaginationService(session)
    mapper = MeanMaintenanceMapper()

    if mainteniance_by_classroom_filter :
        classroom, total = mean_maintenance_pagination_service.maintenance_by_classroom()
        return mapper.to_classroom(classroom, total)
    elif date_filter :
        mean_maintenances = mean_maintenance_pagination_service.maintenace_average()
        return mapper.to_date(mean_maintenances)
    else :
        mean_maintenances = mean_maintenance_pagination_service.get_mean_maintenance(filter_params=filters)

        if not mean_maintenances :
            return []
    
        mean_maintenances_mapped = []
        
        for maintenance in mean_maintenances :
            mean_maintenances_mapped.append(mapper.to_api(maintenance))
        
    return mean_maintenances_mapped


@router.patch(
    "/mean_maintenance/{id}",
    response_model=MeanMaintenanceModel,
    status_code=status.HTTP_200_OK
)
@authorize(role=["administrator"])
async def update_mean_maintenance(
    request: Request,
    id : str,
    filters: MeanMaintenanceChangeRequest,
    current_user : UserModel = Depends(get_current_user),
    session: Session = Depends(get_db)
) :
    mean_maintenance_pagination_service = MeanMaintenancePaginationService(session)
    mean_update_service = MeanMaintenanceUpdateService(session)
    mapper = MeanMaintenanceMapper()

    mean = mean_maintenance_pagination_service.get_mean_maintenance_by_id(id = id)
    
    if not mean :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no maintenance with that id"
        )
    
    mean_updated = mean_update_service.update_one(changes=filters, mean_maintenance=mean)
    
    return mapper.to_api(mean_updated)


@router.delete(
    "/mean_maintenance/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_mean_maintenance(
    id: str,
    session: Session = Depends(get_db)
) :
    mean_maintenance_pagination_service = MeanMaintenancePaginationService(session)
    mean_maintenance_delete_service = MeanMaintenanceDeleteService(session)

    mean =mean_maintenance_pagination_service.get_mean_maintenance_by_id(id=id)

    if not mean :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no mean maintenance with that id"
        )
    
    mean_maintenance_delete_service.delete(mean_maintenance=mean)