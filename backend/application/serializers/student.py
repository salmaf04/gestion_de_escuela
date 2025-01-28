from backend.domain.schemas.student import StudentModel, StudentAcademicPerformance, StudentSubjectPerformance
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
            hash_password= student.hash_password,
            course_year = student.course_year 
        )
        
    def to_academic_performance(self, data) :
        started = False
        
        for average in data :
            if not started :
                started = True
                student = StudentAcademicPerformance(
                    id = average.id,
                    performance = [
                        StudentSubjectPerformance(
                            subject_id = average.subject_id,
                            average_subject_performance = average.academic_performance
                        )
                    ]
                )
            else :
                student.performance.append(
                    StudentSubjectPerformance(
                        subject_id = average.subject_id,
                        average_subject_performance = average.academic_performance
                    )
                )
                
        return student
    
    def to_student_by_teacher(self, data) :
        serialized_students = []

        for tuple in data : 
            student = StudentModel(
                id = tuple[3].id,
                name= tuple[3].name,
                age= tuple[3].age,
                email= tuple[3].email,
                extra_activities= tuple[3].extra_activities,  
                username= tuple[3].username,
                hash_password= tuple[3].hash_password,
                course_year = tuple[3].course_year 
            )
            serialized_students.append(student)
        return serialized_students



