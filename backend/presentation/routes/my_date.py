from backend.application.serializers.my_date import DateMapper
from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from fastapi import Depends, HTTPException, status
from backend.domain.schemas.my_date import DateModel, DateCreateModel
from backend.application.services.my_date import DateCreateService, DatePaginationService
from sqlalchemy.orm import Session
from backend.configuration import get_db


router = APIRouter()


@router.post(
    "/my_date",
    response_model=DateModel,
    status_code=status.HTTP_201_CREATED
)
async def create_date(
    model_input: DateCreateModel,
    session: Session = Depends(get_db)
) :
    date_service = DateCreateService(session)
    mapper = DateMapper()

    response = date_service.create_date(date=model_input)

    return mapper.to_api(response)

@router.get(
    "/my_date/{id}",
    response_model=DateModel,
    status_code=status.HTTP_200_OK
)
async def read_date(
    session: Session = Depends(get_db)
) :
    date_pagination_service = DatePaginationService(session)
    mapper = DateMapper()

    date = date_pagination_service.get_date_by_id(id=id)

    if not date :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no date with that id"
        )
        
    return mapper.to_api(date)