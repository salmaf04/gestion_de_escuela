from fastapi import FastAPI
from .presentation.routes.auth import router as auth_router
from .presentation.routes.administrador import router as admin_router
from .presentation.routes.teacher import router as teacher_router
from .presentation.routes.student import router as student_router
from .presentation.routes.secretary import router as secretary_router
from .presentation.routes.mean import router as mean_router
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from backend.domain.models import tables
from sqlalchemy.orm import sessionmaker

app = FastAPI()

app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(teacher_router)
app.include_router(student_router)
app.include_router(secretary_router)
app.include_router(mean_router)

load_dotenv()

database_url = os.getenv("DATABASE_URL")


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

