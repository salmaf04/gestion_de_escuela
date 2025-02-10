from backend.domain.schemas.valoration import ValorationModel, TeacherValoration, TeacherSubjectValoration
from backend.domain.models.tables import TeacherNoteTable
from backend.application.serializers.teacher import TeacherMapper
from backend.application.serializers.student import StudentMapper
from backend.application.serializers.subject import SubjectMapper
from backend.application.serializers.course import CourseMapper

"""
This module defines a mapper for converting valoration data into API representations.

Classes:
    ValorationMapper: A utility class for mapping TeacherNoteTable objects to ValorationModel objects and handling valorations by subject.

Class Details:

ValorationMapper:
    - This class provides methods to convert TeacherNoteTable objects and related data into various API models used in the application layer.
    
    Methods:
        - to_api(valoration: TeacherNoteTable) -> ValorationModel: 
            Converts the given TeacherNoteTable object into a ValorationModel object, mapping fields such as ID, teacher ID, student ID, subject ID, course ID, and grade.
        - to_valoration_by_subject(data): 
            Converts raw data into a TeacherValoration object, which includes a list of TeacherSubjectValoration objects representing subject-specific valorations. It initializes the TeacherValoration object with the first entry and appends subsequent subject performances.

Dependencies:
    - ValorationModel, TeacherValoration, and TeacherSubjectValoration for API data representation.
    - TeacherNoteTable for database representation.
"""
class ValorationMapper :

    def to_api(self, data) -> ValorationModel :
        teacher_mapper = TeacherMapper()
        subject_mapper = SubjectMapper()
        student_mapper = StudentMapper()
        course_mapper = CourseMapper()

        if isinstance(data, TeacherNoteTable) :
            valoration = data
            note = valoration.grade
           
            mapped_valoration =  ValorationModel(
                id = valoration.entity_id,
                teacher = teacher_mapper.to_api(valoration.teacher),
                student=  student_mapper.to_api((valoration.student, valoration.course)),
                subject = subject_mapper.to_api(valoration.subject),
                course = course_mapper.to_api(valoration.course),
                grade = note
            )
            return mapped_valoration
        else :     
            note = data[1]
            valoration = data[0]

            mapped_valoration =  ValorationModel(
                id = valoration.entity_id,
                teacher = teacher_mapper.to_api(valoration.teacher),
                student= student_mapper.to_api((valoration.student, valoration.course)) if valoration.student else None,
                subject = subject_mapper.to_api(valoration.subject),
                course = course_mapper.to_api(valoration.course),
                grade = note
            )
            return mapped_valoration
    
    def to_valoration_by_subject(self, data) :
        started = False
        
        for average in data :
            if not started :
                started = True
                student = TeacherValoration(
                    id = average.teacher_id,
                    performance = [
                        TeacherSubjectValoration(
                            subject_id = average.subject_id,
                            average_subject_performance = average.valoration
                        )
                    ]
                )
            else :
                student.performance.append(
                    TeacherSubjectValoration(
                        subject_id = average.subject_id,
                        average_subject_performance = average.valoration
                    )
                )
                
        return student