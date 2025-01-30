from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.mean_maintenance import MeanMaintenanceCreateModel, MeanMaintenanceModel
from sqlalchemy.orm import Session
from backend.application.services.mean_maintenance import MeanMaintenanceCreateService, MeanMaintenancePaginationService, MeanMaintenanceUpdateService
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
    mean_maintenance_service = MeanMaintenanceCreateService()
    mapper = MeanMaintenanceMapper()

    response = mean_maintenance_service.create_mean_maintenance(session=session, mean_maintenance=mean_maintenance_input)

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
    mean_maintenance_pagination_service = MeanMaintenancePaginationService()
    mapper = MeanMaintenanceMapper()

    if mainteniance_by_classroom_filter :
        classroom, total = mean_maintenance_pagination_service.maintenance_by_classroom(session=session)
        return mapper.to_classroom(classroom), {"total maintenances after two years" : total }
    elif date_filter :
        mean_maintenances = mean_maintenance_pagination_service.maintenace_average(session=session)
        return mapper.to_date(mean_maintenances)
    else :
        mean_maintenances = mean_maintenance_pagination_service.get_mean_maintenance(session=session, filter_params=filters)

        if not mean_maintenances :
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="There is no mean_maintenance with that fields"
            )
    
        mean_maintenances_mapped = {}    
     
        for i, mean_maintenance in enumerate(mean_maintenances) :
            mean_maintenances_mapped[i] = mapper.to_api(mean_maintenance)
        
    return mean_maintenances_mapped


@router.patch(
    "/mean_maintenance/{id}",
    response_model=MeanMaintenanceModel,
    status_code=status.HTTP_200_OK
)
@authorize(role=["administrator"])
async def update_teacher(
    request: Request,
    id : str,
    filters: MeanMaintenanceChangeRequest,
    current_user : UserModel = Depends(get_current_user),
    session: Session = Depends(get_db)
) :
    mean_maintenance_pagination_service = MeanMaintenancePaginationService()
    mean_update_service = MeanMaintenanceUpdateService()
    mapper = MeanMaintenanceMapper()

    mean = mean_maintenance_pagination_service.get_mean_maintenance_by_id(session=session, id = id)
    
    if not mean :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no maintenance with that id"
        )
    
    mean_model = mapper.to_api(mean)
    
    mean_updated = mean_update_service.update_one(session=session, changes=filters, mean_maintenance=mean_model)

    return mean_updated