from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.administrador import AdministratorCreateModel, AdministratorModel
from sqlalchemy.orm import Session
from backend.application.services.administrador import AdministratorCreateService, AdministratorPaginationService
from fastapi.exceptions import HTTPException
from backend.application.serializers.administrador import AdministratorMapper
from backend.domain.models.config import SessionLocal, engine
from backend.domain.models import tables
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.domain.filters.administrador import ChangeRequest
from backend.application.services.administrador import AdministradorUpdateService, AdministratorPaginationService, AdministratorDeletionService

import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")


engine = create_engine(
    database_url
)
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    database_url
)
tables.BaseTable.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/administrator",
    response_model= AdministratorModel,
    status_code=status.HTTP_201_CREATED
)
async def create_administrator(
    administrator_input: AdministratorCreateModel,
    session: Session = Depends(get_db)
) :
    administrator_service = AdministratorCreateService()
    administrator_pagination_service = AdministratorPaginationService()
    mapper = AdministratorMapper()

    administrator = administrator_pagination_service.get_administrator_by_email(session=session, email=administrator_input.email)

    if administrator :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="There is already an administrator with that email"
        )

    response = administrator_service.create_administrator(session=session, administrator=administrator_input)

    return mapper.to_api(response)

@router.delete(
    "/administrator/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_administrator(
    id: str,
    session: Session = Depends(get_db)
) :
    administrator_pagination_service = AdministratorPaginationService()
    administrator_deletion_service = AdministratorDeletionService()

    administrator =administrator_pagination_service.get_administrator_by_email(session=session, id=id)

    if not administrator :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no administrator with that email"
        )

    administrator_deletion_service.delete_administrator(session=session, administrator=administrator)

@router.patch(
    "/administrator/{id}",
    response_model=AdministratorModel,
    status_code=status.HTTP_200_OK
)
async def update_administrator(
    id : str,
    filters: ChangeRequest = Depends(),
    session: Session = Depends(get_db)
) :
    administrator_pagination_service = AdministratorPaginationService()
    administrator_update_service = AdministradorUpdateService()
    mapper = AdministratorMapper()

    administrator = administrator_pagination_service.get_administrator_by_id(session=session, id = id)
    administrator_model = mapper.to_api(administrator)

    if not administrator :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no administrator with that id"
        )
    print(filters.specialty)

    administrator_updated = administrator_update_service.update_one(session=session, changes=filters, administrator=administrator_model)

    return administrator_updated