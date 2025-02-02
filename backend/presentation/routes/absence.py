from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.absence import AbsenceCreateModel, AbsenceModel
from sqlalchemy.orm import Session
from backend.application.services.absence import AbsenceCreateService, AbsencePaginationService
from fastapi.exceptions import HTTPException
from backend.application.serializers.absence import AbsenceMapper
from backend.configuration import get_db
from backend.domain.filters.absence import AbsenceFilterSchema

router = APIRouter()

@router.post(
    "/absence",
    response_model=AbsenceModel,
    status_code=status.HTTP_201_CREATED
)
async def create_absence(
    absence_input: AbsenceCreateModel,
    session: Session = Depends(get_db)
) :
    absence_service = AbsenceCreateService(session)
    mapper = AbsenceMapper()

    response = absence_service.create_absence(absence=absence_input)

    return mapper.to_api(response)

@router.get(
    "/absence",
    response_model=list[AbsenceModel] | list | dict,
    status_code=status.HTTP_200_OK
)
async def read_absence(
    by_student : str = None,
    by_student_by_teacher : str = None,
    filters: AbsenceFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    absence_pagination_service = AbsencePaginationService(session)
    mapper = AbsenceMapper()

    absences = absence_pagination_service.get_absence(filter_params=filters)

    if not absences :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no absence with that fields"
        )
    
    if by_student :
        absences = absence_pagination_service.get_absence_by_student(student_id=by_student)
        return mapper.to_abscence_by_student(absences)
    elif by_student_by_teacher :
        absences = absence_pagination_service.get_absence_by_student_by_teacher(teacher_id=by_student_by_teacher)
        return mapper.to_absence_by_student_by_teacher(absences)
    
    mapped_absences = []

    for absence in absences :
        mapped_absences.append(mapper.to_api(absence))

    return mapped_absences
