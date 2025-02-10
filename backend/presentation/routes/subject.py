from fastapi import  HTTPException, status, Depends, APIRouter
from backend.domain.schemas.subject import  SubjectModel, SubjectCreateModel
from sqlalchemy.orm import Session
from backend.application.services.subject import SubjectCreateService, SubjectPaginationService, SubjectDeletionService, SubjectUpdateService
from fastapi.exceptions import HTTPException
from backend.application.serializers.subject import SubjectMapper, SubjectByTeacher
from backend.domain.filters.subject import SubjectFilterSchema, SubjectChangeRequest
from backend.configuration import get_db
from backend.presentation.utils.auth import authorize
from fastapi import Request
from backend.domain.schemas.user import UserModel
from backend.presentation.utils.auth import get_current_user

"""
This module defines API endpoints for managing subjects using FastAPI.

Endpoints:
- POST /subject: Create a new subject. Ensures no duplicate subject names.
- DELETE /subject/{id}: Delete an existing subject by its ID.
- GET /subject: Retrieve a list of subjects based on provided filters, including options for subjects by students or teachers. Requires authorization for roles 'secretary', 'teacher', or 'student'.
- PATCH /subject/{id}: Update an existing subject by its ID.

Dependencies:
- FastAPI's APIRouter for routing.
- SQLAlchemy's Session for database interactions.
- Custom services and models for handling subject operations.
- Authorization utilities for role-based access control.

Functions:
- create_subject: Handles the creation of a new subject. Validates that no subject with the same name exists.
- delete_subject: Handles the deletion of a subject. Validates the existence of the subject and deletes it if valid.
- read_subject: Retrieves subjects based on filter criteria, including options for subjects by students or teachers.
- update_subject: Updates an existing subject. Validates the existence of the subject and applies changes if valid.

Parameters:
- subject_input (SubjectCreateModel): The data for creating a new subject.
- id (str): The ID of the subject to delete or update.
- subjects_by_students (str): The ID of the student to filter subjects by.
- subjects_by_teacher (str): The ID of the teacher to filter subjects by.
- filters (SubjectFilterSchema): The filter criteria for retrieving subjects.
- session (Session): The database session dependency.
- current_user (UserModel): The current authenticated user.

Returns:
- JSON responses with the created, retrieved, or updated subject records.

Raises:
- HTTPException: Raised when a subject is not found or when attempting to create a duplicate, with appropriate HTTP status codes.
"""

router = APIRouter()


@router.post(
    "/subject",
    response_model= SubjectModel,
    status_code=status.HTTP_201_CREATED
)
async def create_subject(
    subject_input: SubjectCreateModel,
    session: Session = Depends(get_db)
) :
    subject_pagination_service = SubjectPaginationService(session)
    subject_service = SubjectCreateService(session)
    mapper = SubjectMapper()

    subject_filter_by_name = SubjectFilterSchema(name=[subject_input.name])
    
    subject_check = subject_pagination_service.get_subjects(filter_params=subject_filter_by_name)
    
    if subject_check :
       for subject in subject_check :
           if subject.course_id == subject_input.course_id :
               raise HTTPException(
                   status_code=status.HTTP_403_FORBIDDEN,
                   detail="There is already a subject with that name and course"
               )

    response = subject_service.create_subject(subject=subject_input)

    return mapper.to_api(response)

@router.delete(
    "/subject/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_subject(
    id: str,
    session: Session = Depends(get_db)
) :
    subject_pagination_service = SubjectPaginationService(session)
    subject_deletion_service = SubjectDeletionService(session)

    subject =subject_pagination_service.get_subject_by_id(id=id)

    if not subject :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no subject with that id"
        )

    subject_deletion_service.delete_subject(subject=subject)

@router.get(
    "/subject",
    response_model=dict[int, SubjectModel] | list[SubjectModel] | SubjectModel | list[SubjectByTeacher],
    status_code=status.HTTP_200_OK
)
@authorize(role=["secretary","teacher", "student", "dean"])
async def read_subject(
    request: Request,
    subjects_by_students : str = None,
    subjects_by_teacher : str = None,
    filters: SubjectFilterSchema = Depends(),
    session: Session = Depends(get_db),
    current_user : UserModel = Depends(get_current_user)
) :
    subject_pagination_service = SubjectPaginationService(session)
    mapper = SubjectMapper()

    subjects = subject_pagination_service.get_subjects(filter_params=filters)

    if subjects_by_students :
        subjects = subject_pagination_service.get_subjects_by_students(student_id=subjects_by_students)
        return mapper.to_subjects_by_students(subjects)
    elif subjects_by_teacher :
        subjects = subject_pagination_service.get_subjects_by_teacher(teacher_id=subjects_by_teacher)
        return mapper.to_subjects_by_teacher(subjects)

    if not subjects :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no subject with that id"
        )

    subjects_mapped = []

    for subject in subjects :
        subjects_mapped.append(mapper.to_api(subject))
        
    return subjects_mapped

@router.patch(
    "/subject/{id}",
    response_model=SubjectModel,
    status_code=status.HTTP_200_OK
)
async def update_subject(
    id : str,
    filter_params: SubjectChangeRequest,
    session: Session = Depends(get_db)
) :
    subject_pagination_service = SubjectPaginationService(session)
    subject_update_service = SubjectUpdateService(session)
    mapper = SubjectMapper()

    subject = subject_pagination_service.get_subject_by_id(id = id)

    if not subject :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no subject with that id"
        )
   
    subject_updated = subject_update_service.update_one(changes=filter_params, subject=subject)

    return mapper.to_api(subject_updated)
