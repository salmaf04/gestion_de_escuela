from backend.domain.schemas.student import StudentModel
from backend.domain.models.tables import StudentTable

class StudentMapper :

    def to_api(self, student: StudentTable) -> StudentModel :
        return StudentModel(
            id = student.entity_id,
            name= student.name,
            age= student.age,
            email= student.email,
            extra_activities= student.extra_activities,  
            username= student.username,
            hash_password= student.hash_password
        )
        

