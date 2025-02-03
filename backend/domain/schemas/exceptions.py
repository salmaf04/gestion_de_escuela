from fastapi import HTTPException

"""
This module defines custom exception classes for handling specific error scenarios in the application.

Classes:
    BaseException: A base class for custom exceptions in the application.
    ValidationException: A custom exception class for handling validation errors.

Class Details:

1. BaseException:
    - Inherits from Python's built-in Exception class.
    - Serves as a base class for defining custom exceptions in the application.
    - Can be extended to include common attributes or methods shared across custom exceptions.

2. ValidationException:
    - Inherits from BaseException.
    - Represents a validation error in the application.
    - Attributes:
        - message: A string containing the error message.
    - Methods:
        - __init__(message): Initializes the exception with a specific error message.
        - __str__() -> str: Returns the error message as a string representation of the exception.

Dependencies:
    - FastAPI's HTTPException for handling HTTP-related exceptions (though not directly used in these classes).
"""
class BaseException(Exception):
    pass

class ValidationException(BaseException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return f"{self.message}"
