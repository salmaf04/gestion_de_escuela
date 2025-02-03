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
@authorize(role=['secretary','teacher', 'student'])
async def read_student(
    request: Request,
    id : str = None,
    teacher_id : str = None,
    academic_performance = False,
    students_by_teacher = False,
    filters: StudentFilterSchema = Depends(),
    session: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
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
