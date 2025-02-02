from fastapi import FastAPI
from .presentation.routes.auth import router as auth_router
from .presentation.routes.administrador import router as admin_router
from .presentation.routes.teacher import router as teacher_router
from .presentation.routes.student import router as student_router
from .presentation.routes.secretary import router as secretary_router
from .presentation.routes.mean import router as mean_router
from .presentation.routes.classroom import router as classroom_router
from .presentation.routes.note import router as note_router
from .presentation.routes.subject import router as subject_router
from .presentation.routes.course import router as course_router
from .presentation.routes.absence import router as absence_router
from .presentation.routes.valoration import router as valoration_router
from .presentation.routes.my_date import router as date_router
from .presentation.routes.mean_maintenance import router as mean_maintenance_router
from .presentation.routes.dean import router as dean_router
from .presentation.routes.sanction import router as sanction_router
from .presentation.routes.mean_request import router as mean_request_router
from .presentation.routes.classroom_request import router as classroom_request_router

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from backend.domain.models import tables
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(teacher_router)
app.include_router(student_router)
app.include_router(secretary_router)
app.include_router(mean_router)
app.include_router(classroom_router)
app.include_router(note_router)
app.include_router(subject_router)
app.include_router(course_router)
app.include_router(absence_router)
app.include_router(valoration_router)
app.include_router(date_router)
app.include_router(mean_maintenance_router)
app.include_router(dean_router)
app.include_router(sanction_router)
app.include_router(mean_request_router)
app.include_router(classroom_request_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

database_url = "postgresql+psycopg2://local:local@localhost:5432/testing_school"


engine = create_engine(
    database_url
)

tables.BaseTable.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()