from fastapi import FastAPI, HTTPException, status, Depends
from .schemas import SecretaryCreateModel, SecretaryModel
from sqlalchemy.orm import Session
from .services import SecretaryCreateService, SecretaryPaginationService
from fastapi.exceptions import HTTPException
from .serializers import SecretaryMapper
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