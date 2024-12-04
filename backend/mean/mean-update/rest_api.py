from fastapi import FastAPI, HTTPException, status, Depends
from mean.mean_common.schemas import MeanModel
from sqlalchemy.orm import Session
from .services import MeanUpdateService, MeanListingService
from fastapi.exceptions import HTTPException
from database.config import SessionLocal, engine
from database import tables
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .filters import ChangeRequest
from .serializers import MeanMapper


SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/proyecto"
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
    "/mean/{id}",
    response_model=MeanModel,
    status_code=status.HTTP_200_OK
)
async def mean_update(
    id : str,
    filters: ChangeRequest = Depends(),
    session: Session = Depends(get_db)
) :
    mean_pagination_service = MeanListingService()
    mean_update_service = MeanUpdateService()
    mapper = MeanMapper()

    mean = mean_pagination_service.get_mean_by_id(session=session, id = id)
    mean_model = mapper.to_api(mean)

    if not mean :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no mean with that id"
        )

    mean_updated = mean_update_service.update_one(session=session, changes=filters, mean=mean_model)

    return mean_updated