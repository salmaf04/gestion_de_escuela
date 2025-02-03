from backend.domain.schemas.subject import SubjectModel
from backend.domain.models.tables import SubjectTable

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

class SubjectMapper :

    def to_api(self, subject: SubjectTable) -> SubjectModel :
        return SubjectModel(
            id = subject.entity_id,
            name= subject.name,
            hourly_load= subject.hourly_load,
            study_program= subject.study_program,
            classroom_id= subject.classroom_id if subject.classroom_id else None,
            course_id = subject.course_id
        )
    
    def to_subjects_by_students(self, data) :
        serialized_values = []

        for subject in data :
            new_subject = SubjectModel(
                id = subject[0].entity_id,
                name= subject[0].name,
                hourly_load= subject[0].hourly_load,
                study_program= subject[0].study_program,
                classroom_id= subject[0].classroom_id if subject[0].classroom_id else None,
                course_id = subject[0].course_id
            )
            serialized_values.append(new_subject)

        return serialized_values
    
    def to_subjects_by_teacher(self, data) :
        serialized_values = []

        for subject in data :
            new_subject = SubjectModel(
                id = subject[0].entity_id,
                name= subject[0].name,
                hourly_load= subject[0].hourly_load,
                study_program= subject[0].study_program,
                classroom_id= subject[0].classroom_id if subject[0].classroom_id else None,
                course_id = subject[0].course_id
            )
            serialized_values.append(new_subject)

        return serialized_values
        