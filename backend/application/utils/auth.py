from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Hash password
def get_password_hash(password):
    return pwd_context.hash(password)

def get_password(schema: BaseModel) -> str:
    name = schema.name
    username = schema.username
    lastname = schema.fullname 
    today_date = datetime.now()
    today = today_date.strftime("%d-%m-%Y")

    new_password = name[0].tolower() + username[0].tolower() + lastname[0].tolower() + today
    return new_password
