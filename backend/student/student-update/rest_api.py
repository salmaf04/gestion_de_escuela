from fastapi import FastAPI, HTTPException, status, Depends
from student.student_common.schemas import  StudentModel
from sqlalchemy.orm import Session
from .services import StudentListingService, StudentUpdateService
from fastapi.exceptions import HTTPException
from database.config import SessionLocal, engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .filters import ChangeRequest
from .serializers import StudentMapper


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
    "/student/{id}",
    response_model=StudentModel,
    status_code=status.HTTP_200_OK
)
async def update_student(
    id : str,
    filters: ChangeRequest = Depends(),
    session: Session = Depends(get_db)
) :
    student_pagination_service = StudentListingService()
    student_update_service = StudentUpdateService()
    mapper = StudentMapper()

    student = student_pagination_service.get_student_by_id(session=session, id = id)
    student_model = mapper.to_api(student)

    if not student :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no student with that id"
        )
    print(filters.specialty)

    student_updated = student_update_service.update_one(session=session, changes=filters, student=student_model)

    return student_updated