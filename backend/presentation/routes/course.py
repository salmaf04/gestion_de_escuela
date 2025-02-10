from fastapi import  HTTPException, status, Depends, APIRouter
from backend.domain.schemas.course import  CourseModel, CourseCreateModel
from sqlalchemy.orm import Session
from backend.application.services.course import CourseCreateService, CoursePaginationService, CourseDeletionService, CourseUpdateService
from fastapi.exceptions import HTTPException
from backend.application.serializers.course import CourseMapper
from backend.domain.filters.course import CourseFilterSchema, CourseChangeRequest
from backend.configuration import get_db

"""
This module defines API endpoints for managing courses using FastAPI.

Endpoints:
- POST /course: Create a new course.
- DELETE /course/{id}: Delete an existing course by its ID.
- GET /course: Retrieve a list of courses based on provided filters.
- PATCH /course/{id}: Update an existing course by its ID.

Dependencies:
- FastAPI's APIRouter for routing.
- SQLAlchemy's Session for database interactions.
- Custom services and models for handling course operations.

Functions:
- create_course: Handles the creation of a new course. Utilizes the CourseCreateService to add a course to the database.
- delete_course: Handles the deletion of a course. Validates the existence of the course and deletes it if valid.
- read_course: Retrieves a list of courses based on filter criteria. Utilizes the CoursePaginationService to fetch data.
- update_subject: Updates an existing course. Validates the existence of the course and applies changes if valid.

Raises:
- HTTPException: Raised when a course is not found, with appropriate HTTP status codes.
"""

router = APIRouter()


@router.post(
    "/course",
    response_model= CourseModel,
    status_code=status.HTTP_201_CREATED
)
async def create_course(
    course_input: CourseCreateModel,
    session: Session = Depends(get_db)
) :
    course_service = CourseCreateService(session)
    couse_pagination_service = CoursePaginationService(session)
    mapper = CourseMapper()

    course_check = couse_pagination_service.get_course(
        filter_params=CourseFilterSchema(year=course_input.year)
    )

    if course_check :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="There is already a course with that year"
        )

    response = course_service.create_course(course=course_input)

    return mapper.to_api(response)

@router.delete(
    "/course/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_course(
    id: str,
    session: Session = Depends(get_db)
) :
    course_pagination_service = CoursePaginationService(session)
    course_deletion_service = CourseDeletionService(session)

    course =course_pagination_service.get_course_by_id(id=id)

    if not course :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no course with that id"
        )

    course_deletion_service.delete_course(course=course)

@router.get(
    "/course",
    response_model=list[CourseModel],
    status_code=status.HTTP_200_OK
)
async def read_course(
    filters: CourseFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    course_pagination_service = CoursePaginationService(session)
    mapper = CourseMapper()

    courses = course_pagination_service.get_course(filter_params=filters)

    if not courses :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no course with that id"
        )

    courses_mapped = []

    for course in courses :
        courses_mapped.append(mapper.to_api(course))

    return courses_mapped

@router.patch(
    "/course/{id}",
    response_model=CourseModel,
    status_code=status.HTTP_200_OK
)
async def update_subject(
    id : str,
    filters: CourseChangeRequest,
    session: Session = Depends(get_db)
) :
    course_pagination_service = CoursePaginationService(session)
    course_update_service = CourseUpdateService(session)
    mapper = CourseMapper()

    course = course_pagination_service.get_course_by_id(id = id)
    course_model = mapper.to_api(course)

    if not course :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no course with that id"
        )
    
    course_updated = course_update_service.update_one(changes=filters, course=course_model)

    return course_updated
