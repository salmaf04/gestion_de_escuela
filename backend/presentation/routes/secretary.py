from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from backend.domain.schemas.secretary import SecretaryModel, SecretaryCreateModel
from sqlalchemy.orm import Session
from backend.application.services.secretary import SecretaryCreateService, SecretaryPaginationService, SecretaryDeletionService, SecretaryUpdateService
from fastapi.exceptions import HTTPException
from backend.application.serializers.secretary import SecretaryMapper
from backend.domain.filters.secretary import SecretaryChangeRequest
from backend.configuration import get_db


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
    secretary_service = SecretaryCreateService()
    secretary_pagination_service = SecretaryPaginationService()
    mapper = SecretaryMapper()

    secretary = secretary_pagination_service.get_secretary_by_email(session=session, email=secretary_input.email)

    if secretary :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="There is already an secretary with that email"
        )

    response = secretary_service.create_secretary(session=session, secretary=secretary_input)

    return mapper.to_api(response)

@router.delete(
    "/secretary/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_secretary(
    id: str,
    session: Session = Depends(get_db)
) :
    secretary_pagination_service = SecretaryPaginationService()
    secretary_deletion_service = SecretaryDeletionService()

    secretary =secretary_pagination_service.get_secretary_by_id(session=session, id=id)

    if not secretary :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no secretary with that email"
        )

    secretary_deletion_service.delete_secretary(session=session, secretary=secretary)
    
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
    secretary_pagination_service = SecretaryPaginationService()
    secretary_update_service = SecretaryUpdateService()
    mapper = SecretaryMapper()

    secretary = secretary_pagination_service.get_secretary_by_id(session=session, id = id)
    secretary_model = mapper.to_api(secretary)

    if not secretary :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no secretary with that id"
        )
    print(filters.specialty)

    secretary_updated = secretary_update_service.update_one(session=session, changes=filters, secretary=secretary_model)

    return secretary_updated

    

