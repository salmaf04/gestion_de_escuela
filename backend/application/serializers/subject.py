from backend.domain.schemas.subject import SubjectModel
from backend.domain.models.tables import SubjectTable

class SubjectMapper :

    def to_api(self, subject: SubjectTable) -> SubjectModel :
        return SubjectModel(
            id = subject.entity_id,
            name= subject.name,
            hourly_load= subject.hourly_load,
            study_program= subject.study_program,
            classroom_id= subject.classroom_id,
            course_year= subject.course_year
        )
        