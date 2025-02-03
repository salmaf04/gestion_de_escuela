from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.administrador import AdministratorCreateModel, AdministratorModel
from sqlalchemy.orm import Session
from backend.application.services.administrador import AdministratorCreateService, AdministratorPaginationService
from fastapi.exceptions import HTTPException
from backend.application.serializers.administrador import AdministratorMapper
from backend.domain.filters.administrador import AdministratorChangeRequest, AdministratorFilterSchema, AdministratorFilterSet
from backend.application.services.administrador import AdministradorUpdateService, AdministratorPaginationService, AdministratorDeletionService
from backend.configuration import get_db


router = APIRouter()

@router.post(
    "/administrator",
    response_model= AdministratorModel,
    status_code=status.HTTP_201_CREATED
)
async def create_administrator(
    administrator_input: AdministratorCreateModel,
    session: Session = Depends(get_db)
) :
    administrator_service = AdministratorCreateService(session)
    administrator_pagination_service = AdministratorPaginationService(session)
    mapper = AdministratorMapper()

    administrator = administrator_pagination_service.get(AdministratorFilterSchema())

    if administrator :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Ya existe un adminitrador"
        )

    response = administrator_service.create_administrator(administrator=administrator_input)

    return mapper.to_api(response)

@router.delete(
    "/administrator/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_administrator(
    id: str,
    session: Session = Depends(get_db)
) :
    administrator_pagination_service = AdministratorPaginationService(session)
    administrator_deletion_service = AdministratorDeletionService(session)

    administrator =administrator_pagination_service.get_administrator_by_id(id=id)

    if not administrator :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no administrator with that email"
        )

    administrator_deletion_service.delete_administrator(administrator=administrator)

@router.patch(
    "/administrator/{id}",
    response_model=AdministratorModel,
    status_code=status.HTTP_200_OK
)
async def update_administrator(
    id : str,
    filters: AdministratorChangeRequest ,
    session: Session = Depends(get_db)
) :
    administrator_pagination_service = AdministratorPaginationService(session)
    administrator_update_service = AdministradorUpdateService(session)
    mapper = AdministratorMapper()

    administrator = administrator_pagination_service.get_administrator_by_id(id = id)
    administrator_model = mapper.to_api(administrator)

    if not administrator :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no administrator with that id"
        )
    print(filters.specialty)

    administrator_updated = administrator_update_service.update_one(changes=filters, administrator=administrator_model)

    return administrator_updated

@router.get(
    "/administrator",
    response_model=list[AdministratorModel] | AdministratorModel,
    status_code=status.HTTP_200_OK
)
async def read_administrator(
    filters: AdministratorFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :

    administrtor_pagination_service = AdministratorPaginationService(session)

    administrator = administrtor_pagination_service.get(filter_params=filters)

    if not administrator :
        return []
    
    administrator_mapped = []

    for administrator in administrator :
        administrator_mapped.append(AdministratorMapper().to_api(administrator))
        
    return administrator_mapped