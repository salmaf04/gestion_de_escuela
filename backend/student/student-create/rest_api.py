from fastapi import FastAPI, HTTPException, status, Depends
from .schemas import StudentCreateModel, StudentModel
from sqlalchemy.orm import Session
from .services import StudentCreateService, StudentPaginationService
from fastapi.exceptions import HTTPException
from .serializers import StudentMapper
from datetime import timedelta
from fastapi.responses import JSONResponse
from database.config import SessionLocal, engine
from database import tables

tables.BaseTable.metadata.create_all(bind=engine)


app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post(
    "/student",
    response_model= StudentModel,
    status_code=status.HTTP_201_CREATED
)
async def create_student(
    student_input: StudentCreateModel,
    session: Session = Depends(get_db)
) :
    student_service = StudentCreateService()
    student_pagination_service = StudentPaginationService()
    mapper = StudentMapper()

    student = student_pagination_service.get_student_by_email(session=session, email=student_input.email)

    if student :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="There is already an student with that email"
        )

    response = student_service.create_student(session=session, student=student_input)

    return mapper.to_api(response)