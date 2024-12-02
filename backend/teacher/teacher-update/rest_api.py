from fastapi import FastAPI, HTTPException, status, Depends
from teacher.teacher_common.schemas import  TeacherModel
from sqlalchemy.orm import Session
from .services import TeacherListingService, TeacherUpdateService
from fastapi.exceptions import HTTPException
from database.config import SessionLocal, engine
from database import tables
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .filters import ChangeRequest
from .serializers import TeacherMapper


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
    "/teacher/{id}",
    response_model=TeacherModel,
    status_code=status.HTTP_200_OK
)
async def update_teacher(
    id : str,
    filters: ChangeRequest = Depends(),
    session: Session = Depends(get_db)
) :
    teacher_pagination_service = TeacherListingService()
    teacher_update_service = TeacherUpdateService()
    mapper = TeacherMapper()

    teacher = teacher_pagination_service.get_teacher_by_id(session=session, id = id)
    teacher_model = mapper.to_api(teacher)

    if not teacher :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no teacher with that id"
        )
    print(filters.specialty)

    teacher_updated = teacher_update_service.update_one(session=session, changes=filters, teacher=teacher_model)

    return teacher_updated
    
        
    