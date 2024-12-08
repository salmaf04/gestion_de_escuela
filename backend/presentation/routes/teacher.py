from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from backend.domain.schemas.teacher import TeacherCreateModel, TeacherModel
from sqlalchemy.orm import Session
from backend.application.services.teacher import TeacherCreateService, TeacherPaginationService, TeacherDeletionService, TeacherUpdateService
from fastapi.exceptions import HTTPException
from backend.application.serializers.teacher import TeacherMapper
from datetime import timedelta
from fastapi.responses import JSONResponse
from database.config import SessionLocal, engine
from database import tables
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from backend.domain.filters.teacher import TeacherFilterSchema, ChangeRequest

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

tables.BaseTable.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
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

@router.delete(
    "/teacher/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_teacher(
    id: str,
    session: Session = Depends(get_db)
) :
    teacher_pagination_service = TeacherPaginationService()
    teacher_deletion_service = TeacherDeletionService()

    teacher =teacher_pagination_service.get_teacher_by_email(session=session, id=id)

    if not teacher :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no teacher with that email"
        )

    teacher_deletion_service.delete_teacher(session=session, teacher=teacher)
    
@router.get(
    "/teacher",
    response_model=dict[int, TeacherModel],
    status_code=status.HTTP_200_OK
)
async def read_teacher(
    filters: TeacherFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    teacher_pagination_service = TeacherPaginationService()
    mapper = TeacherMapper()

    teachers = teacher_pagination_service.get_teachers(session=session, filter_params=filters)

    if not teachers :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no teacher with that email"
        )

    teachers_mapped = {}    
     
    for i, teacher in enumerate(teachers) :
        teachers_mapped[i] = mapper.to_api(teacher)
        
    return teachers_mapped

@router.patch(
    "/teacher/{id}",
    response_model=TeacherModel,
    status_code=status.HTTP_200_OK
)
async def update_teacher(
    id : str,
    filters: ChangeRequest = Depends(),
    session: Session = Depends(get_db)
) :
    teacher_pagination_service = TeacherPaginationService()
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