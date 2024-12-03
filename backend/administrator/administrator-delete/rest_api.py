from fastapi import FastAPI, HTTPException, status, Depends  
from sqlalchemy.orm import Session
from .services import AdministratorPaginationService, AdministratorDeletionService
from fastapi.exceptions import HTTPException
from database.config import SessionLocal, engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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

@app.delete(
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

    

