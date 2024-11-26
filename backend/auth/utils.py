from passlib.context import CryptContext

passwd_context = CryptContext(schemes=["bcrypt"])


def generate_password_hash(password: str) -> str:
    hash = passwd_context.hash(password)

    return hash


def verify_password(password: str, hashed_password: str) :
    return passwd_context.verify(password,hashed_password)