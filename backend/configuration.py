import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from backend.domain.models import tables
from sqlalchemy.orm import sessionmaker

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
