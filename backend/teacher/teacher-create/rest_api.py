from fastapi import FastAPI, HTTPException, status, Depends
from .schemas import TeacherCreateModel, TeacherModel
from sqlalchemy.orm import Session
from .services import TeacherCreateService, TeacherPaginationService
from fastapi.exceptions import HTTPException
from .serializers import TeacherMapper
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
    "/teacher",
    response_model=TeacherModel,
    status_code=status.HTTP_201_CREATED
)
async def create_teacher(
    teacher_input: TeacherCreateModel,
    session: Session = Depends(get_db)
) :
    teacher_service = TeacherCreateService()
    teacher_pagination_service = TeacherPaginationService()
    mapper = TeacherMapper()

    teacher = teacher_pagination_service.get_teacher_by_email(session=session, email=teacher_input.email)

    if teacher :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="There is already an teacher with that email"
        )

    response = teacher_service.create_teacher(session=session, teacher=teacher_input)

    return mapper.to_api(response)