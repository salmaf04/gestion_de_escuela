from fastapi import FastAPI, HTTPException, status, Depends
from secretary.secretary_common.schemas import  SecretaryModel
from sqlalchemy.orm import Session
from .services import SecretaryListingService, SecretaryUpdateService
from fastapi.exceptions import HTTPException
from database.config import SessionLocal, engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .filters import ChangeRequest
from .serializers import SecretaryMapper


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
    "/secretary/{id}",
    response_model=SecretaryModel,
    status_code=status.HTTP_200_OK
)
async def update_secretary(
    id : str,
    filters: ChangeRequest = Depends(),
    session: Session = Depends(get_db)
) :
    secretary_pagination_service = SecretaryListingService()
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