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

class DbConnection:
    def __init__(self, con_str) -> None:
        self.con_str = con_str
        self.engine = create_engine(con_str)
        self.Session = sessionmaker(self.engine)

# Database URL
database_url = "postgresql+psycopg2://local:local@localhost:5432/testing_school"

engine = create_engine(
    database_url
)

tables.BaseTable.metadata.create_all(engine)
connection = DbConnection(database_url)
session = connection.Session()

class SecretaryFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = SecretaryTable
        sqlalchemy_session = session

    name = 'Luisa'
    lastname = 'Fernandez'
    username = 'luisafer'
    email = 'lui@gmail.com'
    hashed_password = factory.LazyFunction(lambda: get_password_hash(get_password(SecretaryFactory)))
    roles = ARRAY(Roles.SECRETARY.value)
    type = "secretary"

@pytest.fixture(name="client")  
def client_fixture():  
    def get_db():
        db = connection.Session()
        try:
            yield db
        finally:
            db.close()



