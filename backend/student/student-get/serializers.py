from student.student_common.schemas import StudentModel
from database.tables import StudentTable

class StudentMapper:

    def to_api(self, student: StudentTable) -> StudentModel:
        return StudentModel(
            id=student.entity_id,
            name=student.name,
            age=student.age,
            email=student.email,
        )