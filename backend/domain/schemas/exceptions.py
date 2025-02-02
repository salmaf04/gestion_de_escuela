from fastapi import HTTPException

class BaseException(Exception):
    pass

class ValidationException(BaseException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return f"{self.message}"
