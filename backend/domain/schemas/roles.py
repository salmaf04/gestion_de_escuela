from enum import Enum

class Roles(str, Enum ):
    ADMIN = "admin"
    SECRETARY = "secretary" 
    TEACHER = "teacher"
    STUDENT = "student"
    DEAN = "dean"

    @classmethod
    def get_roles_list(cls) :
        return [role.value for role in Roles]
