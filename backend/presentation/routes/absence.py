"""
API routes for managing student absences.
Provides endpoints for creating and retrieving absence records.
"""

from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.absence import AbsenceCreateModel, AbsenceModel
from sqlalchemy.orm import Session
from backend.application.services.absence import AbsenceCreateService, AbsencePaginationService
from fastapi.exceptions import HTTPException
from backend.application.serializers.absence import AbsenceMapper
from backend.configuration import get_db
from backend.domain.filters.absence import AbsenceFilterSchema
from backend.presentation.utils.auth import authorize
from fastapi import Request
from backend.domain.schemas.user import UserModel
from backend.presentation.utils.auth import get_current_user

router = APIRouter()

@router.post(
    "/absence",
    response_model=AbsenceModel,
    status_code=status.HTTP_201_CREATED
)
async def create_absence(
    absence_input: AbsenceCreateModel,
    session: Session = Depends(get_db)
):
    """
    Create a new absence record.
    
    Args:
        absence_input: Absence details to create
        session: Database session
    
    Returns:
        Created AbsenceModel instance
    """
    absence_service = AbsenceCreateService(session)
    mapper = AbsenceMapper()
    response = absence_service.create_absence(absence=absence_input)
    return mapper.to_api(response)

@router.get(
    "/absence",
    response_model=list[AbsenceModel] | list | dict,
    status_code=status.HTTP_200_OK
)
@authorize(role=["secretary","teacher", "student"])
async def read_absence(
    request: Request,
    by_student: str = None,
    by_student_by_teacher: str = None,
    filters: AbsenceFilterSchema = Depends(),
    session: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    """
    Retrieve absence records with optional filtering.
    
    Args:
        request: FastAPI request object
        by_student: Optional student ID to filter absences
        by_student_by_teacher: Optional teacher ID to filter student absences
        filters: Additional filter parameters
        session: Database session
        current_user: Currently authenticated user
    
    Returns:
        List of AbsenceModel instances or filtered absence data
        
    Raises:
        HTTPException: If no absences found matching criteria
    """
    absence_pagination_service = AbsencePaginationService(session)
    mapper = AbsenceMapper()

    absences = absence_pagination_service.get_absence(filter_params=filters)

    if not absences:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no absence with that fields"
        )
    
    if by_student:
        absences = absence_pagination_service.get_absence_by_student(student_id=by_student)
        return mapper.to_abscence_by_student(absences)
    elif by_student_by_teacher:
        absences = absence_pagination_service.get_absence_by_student_by_teacher(teacher_id=by_student_by_teacher)
        return mapper.to_absence_by_student_by_teacher(absences)
    
    mapped_absences = []
    for absence in absences:
        mapped_absences.append(mapper.to_api(absence))

    return mapped_absences
