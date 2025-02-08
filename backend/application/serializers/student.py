from backend.domain.schemas.student import StudentModel, StudentAcademicPerformance, StudentSubjectPerformance
from backend.domain.models.tables import StudentTable
from backend.application.serializers.course import CourseMapper

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

    def to_api(self, student) -> StudentModel :
        course_mapper = CourseMapper()

        return StudentModel(
            id = student[0].entity_id,
            name= student[0].name,
            lastname= student[0].lastname,
            age= student[0].age,
            email= student[0].email,
            extra_activities= student[0].extra_activities,  
            username= student[0].username,
            hash_password= student[0].hashed_password,
            course = course_mapper.to_api(student[1])
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
        course_mapper = CourseMapper()

        for tuple in data : 
            student = StudentModel(
                id = tuple[3].id,
                name= tuple[3].name,
                lastname=tuple[3].lastname,
                age= tuple[3].age,
                email= tuple[3].email,
                extra_activities= tuple[3].extra_activities,  
                username= tuple[3].username,
                hash_password= tuple[3].hashed_password,
                course_id = course_mapper.to_api(tuple[3].course)
            )
            serialized_students.append(student)
        return serialized_students



