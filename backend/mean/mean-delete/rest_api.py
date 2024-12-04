from fastapi import FastAPI, HTTPException, status, Depends  
from sqlalchemy.orm import Session
from .services import MeanPaginationService, MeanDeletionService
from fastapi.exceptions import HTTPException
from database.config import SessionLocal, engine
from database import tables
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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

@app.delete(
    "/mean/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_mean(
    id: str,
    session: Session = Depends(get_db)
) :
    mean_pagination_service = MeanPaginationService()
    mean_deletion_service = MeanDeletionService()

    mean =mean_pagination_service.get_mean_by_id(session=session, id=id)

    if not mean :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no mean with that id"
        )

    mean_deletion_service.delete_mean(session=session, mean=mean)

    

