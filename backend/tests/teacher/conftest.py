from sqlalchemy import create_engine, text
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.orm import sessionmaker
import psycopg2
import pytest
from backend.domain.models import tables
from typing import Generator
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from backend.main_test import app, get_db

# Database URL
database_url = "postgresql+psycopg2://local:local@localhost:5432/testing_school"

engine = create_engine(
    database_url
)

tables.BaseTable.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(name="client")  
def client_fixture():  
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()


