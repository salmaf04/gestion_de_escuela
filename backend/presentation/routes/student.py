from fastapi import  HTTPException, status, Depends, APIRouter
from backend.domain.schemas.student import  StudentModel, StudentCreateModel, StudentAcademicPerformance
from sqlalchemy.orm import Session
from backend.application.services.student import StudentCreateService, StudentPaginationService, StudentDeletionService, StudentUpdateService
from fastapi.exceptions import HTTPException
from backend.application.serializers.student import StudentMapper
from backend.domain.filters.student import StudentFilterSchema, StudentChangeRequest
from backend.configuration import get_db
from backend.presentation.utils.auth import authorize, get_current_user
from backend.domain.schemas.user import UserModel
from fastapi import Request

"""
This module defines API endpoints for managing students using FastAPI.

Endpoints:
- POST /student: Create a new student. Requires authorization for the role 'secretary'.
- DELETE /student/{id}: Delete an existing student by their ID.
- GET /student: Retrieve a list of students based on provided filters, including options for academic performance and students by teacher. Requires authorization for roles 'secretary', 'teacher', or 'student'.
- PATCH /student/{id}: Update an existing student by their ID.

Dependencies:
- FastAPI's APIRouter for routing.
- SQLAlchemy's Session for database interactions.
- Custom services and models for handling student operations.
- Authorization utilities for role-based access control.

Functions:
- create_student: Handles the creation of a new student. Validates that no student with the same email exists.
- delete_student: Handles the deletion of a student. Validates the existence of the student and deletes them if valid.
- read_student: Retrieves students based on filter criteria, including options for academic performance and students by teacher.
- update_student: Updates an existing student. Validates the existence of the student and applies changes if valid.

Parameters:
- student_input (StudentCreateModel): The data for creating a new student.
- id (str): The ID of the student to delete or update.
- teacher_id (str): The ID of the teacher to filter students by.
- academic_performance (bool): Indicates if the user wants to retrieve academic performance information.
- students_by_teacher (bool): Indicates if the user wants to retrieve students by teacher.
- filters (StudentFilterSchema): The filter criteria for retrieving students.
- session (Session): The database session dependency.
- current_user (UserModel): The current authenticated user.

Returns:
- JSON responses with the created, retrieved, or updated student records.

Raises:
- HTTPException: Raised when a student is not found or when attempting to create a duplicate, with appropriate HTTP status codes.
"""

router = APIRouter()



@router.post(
    "/student",
    response_model= StudentModel,
    status_code=status.HTTP_201_CREATED
)
@authorize(role=['secretary'])
async def create_student(
    student_input: StudentCreateModel,
    session: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
) :
    student_service = StudentCreateService(session)
    student_pagination_service = StudentPaginationService(session)
    mapper = StudentMapper()

    student = student_pagination_service.get_student_by_email(email=student_input.email)

    if student :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="There is already an student with that email"
        )

    response = student_service.create_student(student=student_input)

    return mapper.to_api(response)

@router.delete(
    "/student/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_student(
    id: str,
    session: Session = Depends(get_db)
) :
    student_pagination_service = StudentPaginationService(session)
    student_deletion_service = StudentDeletionService(session)

    student =student_pagination_service.get_student_by_id(id=id)

    if not student :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no student with that email"
        )

    student_deletion_service.delete_student(student=student)

@router.get(
    "/student",
    response_model=dict[int, StudentModel] | StudentAcademicPerformance | list[StudentModel],
    status_code=status.HTTP_200_OK
)
@authorize(role=['secretary','teacher', 'student', 'dean'])
async def read_student(
    request: Request,
    id : str = None,
    filters : StudentFilterSchema = Depends(),
    teacher_id : str = None,
    academic_performance = False,
    students_by_teacher = False,
    current_user: UserModel = Depends(get_current_user),
    session: Session = Depends(get_db),
) :
    student_pagination_service = StudentPaginationService(session)
    mapper = StudentMapper()

    if academic_performance :
        students = student_pagination_service.get_academic_information(student_id=id)
        return mapper.to_academic_performance(students)
    elif students_by_teacher :
        students = student_pagination_service.get_students_by_teacher(teacher_id=teacher_id)
        return mapper.to_student_by_teacher(students)

    
    students = student_pagination_service.get_students(filter_params=filters)

    if not students :
        return []

    students_mapped = {}    
     
    
    for i, student in enumerate(students) :
        students_mapped[i] = mapper.to_api(student)
        
    return students_mapped

@router.patch(
    "/student/{id}",
    response_model=StudentModel,
    status_code=status.HTTP_200_OK
)
async def update_student(
    id : str,
    filters: StudentChangeRequest,
    session: Session = Depends(get_db)
) :
    student_pagination_service = StudentPaginationService(session)
    student_update_service = StudentUpdateService(session)
    mapper = StudentMapper()

    student = student_pagination_service.get_student_by_id(id=id)
    
    if not student :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no student with that id"
        )
    
    student_model = mapper.to_api(student)
    student_updated = student_update_service.update_one(changes=filters, student=student_model)

    return student_updated
