from fastapi import  HTTPException, status, Depends, APIRouter
from backend.domain.schemas.course import  CourseModel, CourseCreateModel
from sqlalchemy.orm import Session
from backend.application.services.course import CourseCreateService, CoursePaginationService, CourseDeletionService, CourseUpdateService
from fastapi.exceptions import HTTPException
from backend.application.serializers.course import CourseMapper
from backend.domain.filters.course import CourseFilterSchema, ChangeRequest
from backend.configuration import get_db

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
    course_service = CourseCreateService()
    mapper = CourseMapper()

    response = course_service.create_course(session=session, course=course_input)

    return mapper.to_api(response)

@router.delete(
    "/course/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_course(
    id: str,
    session: Session = Depends(get_db)
) :
    course_pagination_service = CoursePaginationService()
    course_deletion_service = CourseDeletionService()

    course =course_pagination_service.get_course_by_id(session=session, id=id)

    if not course :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no course with that id"
        )

    course_deletion_service.delete_course(session=session, course=course)

@router.get(
    "/course",
    response_model=dict[int, CourseModel],
    status_code=status.HTTP_200_OK
)
async def read_course(
    filters: CourseFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    course_pagination_service = CoursePaginationService()
    mapper = CourseMapper()

    courses = course_pagination_service.get_courses(session=session, filter_params=filters)

    if not courses :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no course with that id"
        )

    courses_mapped = {}    
     
    for i, course in enumerate(courses) :
        courses_mapped[i] = mapper.to_api(course)
        
    return courses_mapped

@router.patch(
    "/course/{id}",
    response_model=CourseModel,
    status_code=status.HTTP_200_OK
)
async def update_subject(
    id : str,
    filters: ChangeRequest = Depends(),
    session: Session = Depends(get_db)
) :
    course_pagination_service = CoursePaginationService()
    course_update_service = CourseUpdateService()
    mapper = CourseMapper()

    course = course_pagination_service.get_course_by_id(session=session, id = id)
    course_model = mapper.to_api(course)

    if not course :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no course with that id"
        )
    print(filters.specialty)

    course_updated = course_update_service.update_one(session=session, changes=filters, course=course_model)

    return course_updated
