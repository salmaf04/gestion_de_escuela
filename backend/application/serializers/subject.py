from backend.domain.schemas.subject import SubjectModel
from backend.domain.models.tables import SubjectTable

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
        