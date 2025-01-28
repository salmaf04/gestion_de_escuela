from backend.domain.schemas.course import CourseModel
from backend.domain.models.tables import CourseTable

class CourseMapper :

    def to_api(self, courses: list[CourseTable]) -> list[CourseModel] :
        serialized_courses = []
        for course in courses :
            serialized_courses.append(CourseModel(
                id = course.entity_id,
                year = course.year
            ))
        return serialized_courses   

        