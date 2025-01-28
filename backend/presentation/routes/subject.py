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
    subject_service = SubjectCreateService()
    mapper = SubjectMapper()

    response = subject_service.create_subject(session=session, subject=subject_input)

    return mapper.to_api(response)

@router.delete(
    "/subject/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_subject(
    id: str,
    session: Session = Depends(get_db)
) :
    subject_pagination_service = SubjectPaginationService()
    subject_deletion_service = SubjectDeletionService()

    subject =subject_pagination_service.get_subject_by_id(session=session, id=id)

    if not subject :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no subject with that id"
        )

    subject_deletion_service.delete_subject(session=session, subject=subject)

@router.get(
    "/subject",
    response_model=dict[int, SubjectModel],
    status_code=status.HTTP_200_OK
)
async def read_subject(
    filters: SubjectFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    subject_pagination_service = SubjectPaginationService()
    mapper = SubjectMapper()

    subjects = subject_pagination_service.get_subjects(session=session, filter_params=filters)

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
    filter_params: SubjectChangeRequest = Depends(),
    session: Session = Depends(get_db)
) :
    subject_pagination_service = SubjectPaginationService()
    subject_update_service = SubjectUpdateService()
    mapper = SubjectMapper()

    subject = subject_pagination_service.get_subject_by_id(session=session, id = id)
    subject_model = mapper.to_api(subject)

    if not subject :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no subject with that id"
        )
    
    print(filter_params)
   
    subject_updated = subject_update_service.update_one(session=session, changes=filter_params, subject=subject_model)

    return subject_updated
