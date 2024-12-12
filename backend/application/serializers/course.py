from backend.domain.schemas.course import CourseModel
from backend.domain.models.tables import CourseTable

class CourseMapper :

    def to_api(self, course:CourseTable) ->CourseModel :
        return CourseModel(
            id = course.entity_id,
            start_year= course.start_year,
            end_year= course.end_year
        )
        