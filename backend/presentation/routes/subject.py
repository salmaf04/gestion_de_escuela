from fastapi import  HTTPException, status, Depends, APIRouter
from backend.domain.schemas.subject import  SubjectModel, SubjectCreateModel
from sqlalchemy.orm import Session
from backend.application.services.subject import SubjectCreateService, SubjectPaginationService, SubjectDeletionService, SubjectUpdateService
from fastapi.exceptions import HTTPException
from backend.application.serializers.subject import SubjectMapper
from backend.domain.filters.subject import SubjectFilterSchema, SubjectChangeRequest
from backend.configuration import get_db

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
    subject_service = SubjectCreateService(session)
    mapper = SubjectMapper()

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
    response_model=dict[int, SubjectModel],
    status_code=status.HTTP_200_OK
)
async def read_subject(
    filters: SubjectFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    subject_pagination_service = SubjectPaginationService(session)
    mapper = SubjectMapper()

    subjects = subject_pagination_service.get_subjects(filter_params=filters)

    if not subjects :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no subject with that id"
        )

    subjects_mapped = {}    
     
    for i, subject in enumerate(subjects) :
        subjects_mapped[i] = mapper.to_api(subject)
        
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
    subject_model = mapper.to_api(subject)

    if not subject :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no subject with that id"
        )
   
    subject_updated = subject_update_service.update_one(changes=filter_params, subject=subject_model)

    return subject_updated
