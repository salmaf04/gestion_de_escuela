from sqlalchemy import create_engine, text
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.orm import sessionmaker
import psycopg2
import pytest
from backend.domain.models import tables
from typing import Generator
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
import factory
from backend.domain.models.tables import SecretaryTable, Roles
from backend.domain.schemas.secretary import SecretaryModel
from backend.domain.schemas.secretary import SecretaryCreateModel
from backend.application.services.secretary import SecretaryCreateService
from backend.application.services.secretary import SecretaryPaginationService
from backend.domain.filters.secretary import SecretaryFilterSchema
from backend.application.utils .auth import get_password_hash, get_password
from sqlalchemy import ARRAY
from backend.main import app
from backend.domain.models.tables import BaseTable
from backend.configuration import get_db


# Database URL
database_url = "postgresql+psycopg2://local:local@localhost:5432/testing_school"

engine = create_engine(database_url)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea las tablas
BaseTable.metadata.create_all(bind=engine)


class SecretaryFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = SecretaryTable
        sqlalchemy_session = engine

    entity_id = "e06236c5-6639-4b48-8942-1acc6319e392"
    name = 'Luisa'
    lastname = 'Fernandez'
    username = 'luisafer'
    email = 'lui@gmail.com'
    hashed_password = factory.LazyFunction(lambda: get_password_hash(get_password(SecretaryFactory)))
    roles = ARRAY(Roles.SECRETARY.value)
    type = "secretary"
    


@pytest.fixture(scope="function")
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c

