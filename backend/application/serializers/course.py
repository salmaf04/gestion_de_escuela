from backend.domain.schemas.course import CourseModel
from backend.domain.models.tables import CourseTable

"""
This module defines a mapper for converting course data into API representations.

Classes:
    CourseMapper: A utility class for mapping CourseTable objects to CourseModel objects.

Class Details:

CourseMapper:
    - This class provides a method to convert a CourseTable object, which represents a database record, into a CourseModel object, which is used in the API layer.
    
    Methods:
        - to_api(courses: CourseTable) -> CourseModel: 
            Converts the given CourseTable object into a CourseModel object, mapping the relevant fields such as ID and year.

Dependencies:
    - CourseModel for API data representation.
    - CourseTable for database representation.
"""

class CourseMapper :

    def to_api(self, courses: CourseTable) -> CourseModel:
        return CourseModel(
            id = courses.entity_id,
            year = courses.year
        )
        