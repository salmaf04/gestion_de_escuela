from fastapi import FastAPI, HTTPException, status, Depends
from student.student_common.schemas import  StudentModel
from sqlalchemy.orm import Session
from .services import StudentListingService
from fastapi.exceptions import HTTPException
from .serializers import StudentMapper
from database.config import SessionLocal, engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .filters import StudentFilterSchema


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


@app.get(
    "/student",
    response_model=dict[int, StudentModel],
    status_code=status.HTTP_200_OK
)
async def read_student(
    filters: StudentFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    student_pagination_service = StudentListingService()
    mapper = StudentMapper()

    students = student_pagination_service.get_students(session=session, filter_params=filters)

    if not students :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no student with that email"
        )

    students_mapped = {}    
     
    for i, student in enumerate(students) :
        students_mapped[i] = mapper.to_api(student)
        
    return students_mapped
