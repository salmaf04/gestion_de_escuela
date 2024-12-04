from fastapi import FastAPI, HTTPException, status, Depends, Query, Request
from typing import Annotated
from mean.mean_common.schemas import  MeanModel
from sqlalchemy.orm import Session
from .services import MeanListingService
from fastapi.exceptions import HTTPException
from .serializers import MeanMapper
from datetime import timedelta
from fastapi.responses import JSONResponse
from database.config import SessionLocal, engine
from database import tables
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .filters import MeanFilterSchema

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5434/proyecto"
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


@app.get(
    "/mean",
    response_model=dict[int, MeanModel],
    status_code=status.HTTP_200_OK
)
async def read_mean(
    filters: MeanFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    mean_pagination_service = MeanListingService()
    mapper = MeanMapper()

    means = mean_pagination_service.get_means(session=session, filter_params=filters)

    if not means :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no means with that fields"
        )

    means_mapped = {}    
     
    for i, means in enumerate(means) :
        means_mapped[i] = mapper.to_api(means)
        
    return means_mapped
