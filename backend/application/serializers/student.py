from backend.domain.schemas.student import StudentModel, StudentAcademicPerformance, StudentSubjectPerformance
from backend.domain.models.tables import StudentTable

"""
This module defines a mapper for converting student data into API representations.

Classes:
    StudentMapper: A utility class for mapping StudentTable objects to various student-related API models.

Class Details:

StudentMapper:
    - This class provides methods to convert StudentTable objects and related data into various API models used in the application layer.
    
    Methods:
        - to_api(student: StudentTable) -> StudentModel: 
            Converts the given StudentTable object into a StudentModel object, mapping fields such as ID, name, lastname, age, email, extra activities, username, hashed password, and course ID.
        - to_academic_performance(data): 
            Converts raw academic performance data into a StudentAcademicPerformance object, which includes a list of StudentSubjectPerformance objects representing subject-specific performance.
        - to_student_by_teacher(data): 
            Converts raw data into a list of StudentModel objects, representing students associated with a specific teacher.

Dependencies:
    - StudentModel, StudentAcademicPerformance, and StudentSubjectPerformance for API data representation.
    - StudentTable for database representation.
"""

class StudentMapper :

    def to_api(self, student: StudentTable) -> StudentModel :
        return StudentModel(
            id = student.entity_id,
            name= student.name,
            lastname= student.lastname,
            age= student.age,
            email= student.email,
            extra_activities= student.extra_activities,  
            username= student.username,
            hash_password= student.hashed_password,
            course_id = student.course_id 
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
                course_id = tuple[3].course_id 
            )
            serialized_students.append(student)
        return serialized_students



