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
    date_service = DateCreateService()
    mapper = DateMapper()

    response = date_service.create_date(session=session, date=model_input)

    return mapper.to_api(response)

@router.get(
    "/my_date",
    response_model=dict[int, DateModel],
    status_code=status.HTTP_200_OK
)
async def read_date(
    session: Session = Depends(get_db)
) :
    date_pagination_service = DatePaginationService()
    mapper = DateMapper()

    dates = date_pagination_service.get_dates(session=session)

    if not dates :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no dates with that fields"
        )

    dates_mapped = {}    
     
    for i, dates in enumerate(dates) :
        dates_mapped[i] = mapper.to_api(dates)
        
    return dates_mapped