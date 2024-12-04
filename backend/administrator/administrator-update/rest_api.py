from fastapi import FastAPI, HTTPException, status, Depends
from administrator.administrator_common.schemas import  AdministratorModel
from sqlalchemy.orm import Session
from .services import AdministratorListingService, AdministratorUpdateService
from fastapi.exceptions import HTTPException
from database.config import SessionLocal, engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .filters import ChangeRequest
from .serializers import AdministratorMapper


SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.patch(
    "/administrator/{id}",
    response_model=AdministratorModel,
    status_code=status.HTTP_200_OK
)
async def update_administrator(
    id : str,
    filters: ChangeRequest = Depends(),
    session: Session = Depends(get_db)
) :
    administrator_pagination_service = AdministratorListingService()
    administrator_update_service = AdministratorUpdateService()
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