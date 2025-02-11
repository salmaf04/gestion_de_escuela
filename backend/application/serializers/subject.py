from backend.domain.schemas.subject import SubjectModel
from backend.domain.models.tables import SubjectTable
from backend.application.serializers.classroom import ClassroomMapper
from backend.application.serializers.course import CourseMapper
from typing import Optional

"""
This module defines a mapper for converting subject data into API representations.

Classes:
    SubjectMapper: A utility class for mapping SubjectTable objects to SubjectModel objects and handling subjects associated with students and teachers.

Class Details:

SubjectMapper:
    - This class provides methods to convert SubjectTable objects and related data into various API models used in the application layer.
    
    Methods:
        - to_api(subject: SubjectTable) -> SubjectModel: 
            Converts the given SubjectTable object into a SubjectModel object, mapping fields such as ID, name, hourly load, study program, classroom ID, and course ID.
        - to_subjects_by_students(data): 
            Converts raw data into a list of SubjectModel objects, representing subjects associated with specific students.
        - to_subjects_by_teacher(data): 
            Converts raw data into a list of SubjectModel objects, representing subjects taught by a specific teacher.

Dependencies:
    - SubjectModel for API data representation.
    - SubjectTable for database representation.
"""

class SubjectByTeacher(SubjectModel) :
    average_note : Optional[float] = None

class SubjectMapper :

    def to_api(self, subject: SubjectTable) -> SubjectModel :
        classroom_mapper = ClassroomMapper()
        course_mapper = CourseMapper()
    
        return SubjectModel(
            id = subject.entity_id,
            name= subject.name,
            hourly_load= subject.hourly_load,
            study_program= subject.study_program,
            classroom = classroom_mapper.to_api_default(subject.classroom) if subject.classroom else None,
            course = course_mapper.to_api(subject.course) if subject.course else None
        )
    
    def to_subjects_by_students(self, data) :
        serialized_values = []
        classroom_mapper = ClassroomMapper()
        course_mapper = CourseMapper()

        for subject in data :
            new_subject = SubjectModel(
                id = subject[0].entity_id,
                name= subject[0].name,
                hourly_load= subject[0].hourly_load,
                study_program= subject[0].study_program,
                classroom = classroom_mapper.to_api_default(subject[0].classroom) if subject[0].classroom else None,
                course = course_mapper.to_api(subject[1]) if subject[1] else None
            )
            serialized_values.append(new_subject)

        return serialized_values
    
    def to_subjects_by_teacher(self, data) :
        serialized_values = []
        classroom_mapper = ClassroomMapper()
        course_mapper = CourseMapper()

        for subject in data :
            new_subject = SubjectByTeacher(
                id = subject[0].entity_id,
                name= subject[0].name,
                hourly_load= subject[0].hourly_load,
                study_program= subject[0].study_program,
                classroom = classroom_mapper.to_api_default(subject[0].classroom) if subject[0].classroom else None,
                course = course_mapper.to_api(subject[0].course) if subject[0].course else None, 
                average_note= subject[1] if subject[1] else None
            )
            serialized_values.append(new_subject)

        return serialized_values
        