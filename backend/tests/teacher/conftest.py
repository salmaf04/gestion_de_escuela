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


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        database_url
    )
    tables.BaseTable.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")  
def client_fixture(session: Session):  
    def get_session_override():  
        return session

    app.dependency_overrides[get_db] = get_session_override  

    client = TestClient(app)  
    yield client  
    app.dependency_overrides.clear()  

