from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.mean_mainteniance import MeanMaintenanceCreateModel, MeanMaintenanceModel
from sqlalchemy.orm import Session
from backend.application.services.mean_mainteniance import MeanMaintenanceCreateService, MeanMaintenancePaginationService
from backend.application.serializers.mean_mainteniance import MeanMaintenanceMapper
from backend.configuration import get_db
from backend.domain.filters.mean_mainteniance import MeanMaintenanceFilterSchema

router = APIRouter()

@router.post(
    "/mean_mainteniance",
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
    "/mean_mainteniance",
    response_model=dict[int, MeanMaintenanceModel],
    status_code=status.HTTP_200_OK
)
async def read_mean_maintenance(
    filters: MeanMaintenanceFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    mean_maintenance_pagination_service = MeanMaintenancePaginationService()
    mapper = MeanMaintenanceMapper()

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