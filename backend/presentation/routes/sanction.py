from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from backend.domain.schemas.sanction import SanctionCreateModel, SanctionModel
from backend.configuration import get_db
from sqlalchemy.orm import Session
from backend.application.services.sanction import SanctionCreateService
from backend.application.serializers.sanction import SanctionMapper

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

    


