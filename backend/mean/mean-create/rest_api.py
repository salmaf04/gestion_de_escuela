from .serializers import MeanMapper
from datetime import timedelta
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi import Depends, HTTPException, status
from database.config import SessionLocal, engine
from database import tables
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .schemas import MeanCreateModel, MeanModel
from .services import MeanCreateService
from sqlalchemy.orm import Session

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/proyecto"
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
    "/mean",
    response_model=MeanModel,
    status_code=status.HTTP_201_CREATED
)
async def create_teacher(
    model_input: MeanCreateModel,
    session: Session = Depends(get_db)
) :
    mean_service = MeanCreateService()
    mapper = MeanMapper()

    response = mean_service.mean_create(session=session, mean=model_input)

    return mapper.to_api(response)