from fastapi import FastAPI, HTTPException, status, Depends, Query, Request
from typing import Annotated
from teacher.teacher_common.schemas import  TeacherModel
from sqlalchemy.orm import Session
from .services import TeacherListingService
from fastapi.exceptions import HTTPException
from .serializers import TeacherMapper
from datetime import timedelta
from fastapi.responses import JSONResponse
from database.config import SessionLocal, engine
from database import tables
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .filters import TeacherFilterSchema
import dataclasses

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
    "/teacher",
    response_model=dict[int, TeacherModel],
    status_code=status.HTTP_200_OK
)
async def read_teacher(
    filters: TeacherFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    teacher_pagination_service = TeacherListingService()
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

