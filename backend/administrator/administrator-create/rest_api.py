from fastapi import FastAPI, HTTPException, status, Depends
from .schemas import AdministratorCreateModel, AdministratorModel
from sqlalchemy.orm import Session
from .services import AdministratorCreateService, AdministratorPaginationService
from fastapi.exceptions import HTTPException
from .serializers import AdministratorMapper
from database.config import SessionLocal, engine
from database import tables
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
tables.BaseTable.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post(
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