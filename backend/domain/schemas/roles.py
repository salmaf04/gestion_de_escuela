from enum import Enum

"""
This module defines an enumeration for user roles in the application.

Classes:
    Roles: An enumeration representing different user roles.

Class Details:

Roles:
    - Inherits from Python's built-in Enum class and str.
    - Represents different user roles in the application.
    - Enum Members:
        - ADMIN: Represents an admin role.
        - SECRETARY: Represents a secretary role.
        - TEACHER: Represents a teacher role.
        - STUDENT: Represents a student role.
        - DEAN: Represents a dean role.
    - Methods:
        - get_roles_list(cls): A class method that returns a list of all role values as strings.

Usage:
    - Use `Roles` to access specific role values, e.g., `Roles.ADMIN`.
    - Use `Roles.get_roles_list()` to retrieve a list of all role values.
"""
class Roles(str, Enum ):
    ADMIN = "admin"
    SECRETARY = "secretary" 
    TEACHER = "teacher"
    STUDENT = "student"
    DEAN = "dean"

    @classmethod
    def get_roles_list(cls) :
        return [role.value for role in Roles]
