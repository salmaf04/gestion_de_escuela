from backend.domain.schemas.course import CourseModel
from backend.domain.models.tables import CourseTable

class CourseMapper :

    def to_api(self, courses: CourseTable) -> CourseModel:
        return CourseModel(
            id = courses.entity_id,
            year = courses.year
        )
        