from fastapi import  HTTPException, status, Depends, APIRouter
from backend.domain.schemas.student import  StudentModel, StudentCreateModel
from sqlalchemy.orm import Session
from backend.application.services.student import StudentCreateService, StudentPaginationService, StudentDeletionService, StudentUpdateService
from fastapi.exceptions import HTTPException
from backend.application.serializers.student import StudentMapper
from backend.domain.filters.student import StudentFilterSchema, ChangeRequest
from backend.configuration import get_db

router = APIRouter()



@router.post(
    "/student",
    response_model= StudentModel,
    status_code=status.HTTP_201_CREATED
)
async def create_student(
    student_input: StudentCreateModel,
    session: Session = Depends(get_db)
) :
    student_service = StudentCreateService()
    student_pagination_service = StudentPaginationService()
    mapper = StudentMapper()

    student = student_pagination_service.get_student_by_email(session=session, email=student_input.email)

    if student :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="There is already an student with that email"
        )

    response = student_service.create_student(session=session, student=student_input)

    return mapper.to_api(response)

@router.delete(
    "/student/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_student(
    id: str,
    session: Session = Depends(get_db)
) :
    student_pagination_service = StudentPaginationService()
    student_deletion_service = StudentDeletionService()

    student =student_pagination_service.get_student_by_email(session=session, id=id)

    if not student :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no student with that email"
        )

    student_deletion_service.delete_student(session=session, student=student)

@router.get(
    "/student",
    response_model=dict[int, StudentModel],
    status_code=status.HTTP_200_OK
)
async def read_student(
    filters: StudentFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    student_pagination_service = StudentPaginationService()
    mapper = StudentMapper()

    students = student_pagination_service.get_students(session=session, filter_params=filters)

    if not students :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no student with that email"
        )

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
    filters: ChangeRequest = Depends(),
    session: Session = Depends(get_db)
) :
    student_pagination_service = StudentPaginationService()
    student_update_service = StudentUpdateService()
    mapper = StudentMapper()

    student = student_pagination_service.get_student_by_id(session=session, id = id)
    student_model = mapper.to_api(student)

    if not student :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no student with that id"
        )
    print(filters.specialty)

    student_updated = student_update_service.update_one(session=session, changes=filters, student=student_model)

    return student_updated
