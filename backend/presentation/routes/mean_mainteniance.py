from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.mean_mainteniance import MeanMaintenanceCreateModel, MeanMaintenanceModel
from sqlalchemy.orm import Session
from backend.application.services.mean_mainteniance import MeanMaintenanceCreateService
from backend.application.serializers.mean_mainteniance import MeanMaintenanceMapper
from backend.configuration import get_db

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