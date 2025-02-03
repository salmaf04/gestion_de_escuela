import uuid
from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from backend.domain.schemas.teacher import TeacherCreateModel, TeacherModel
from sqlalchemy.orm import Session
from backend.application.services.teacher import TeacherCreateService, TeacherPaginationService, TeacherDeletionService, TeacherUpdateService, TeacherSubjectService
from fastapi.exceptions import HTTPException
from backend.application.serializers.teacher import TeacherMapper
from backend.domain.filters.teacher import TeacherFilterSchema, TeacherChangeRequest
from backend.configuration import get_db
from backend.presentation.utils.auth import get_current_user
from backend.domain.schemas.user import UserModel
from backend.presentation.utils.auth import authorize
from fastapi import Request


router = APIRouter()


@router.post(
    "/teacher",
    response_model=TeacherModel | dict[str, str],
    status_code=status.HTTP_201_CREATED
)
@authorize(role=["secretary"])
async def create_teacher(
    request: Request,
    teacher_input: TeacherCreateModel,
    current_user : UserModel = Depends(get_current_user),
    session: Session = Depends(get_db)
) :
    teacher_service = TeacherCreateService(session)
    teacher_pagination_service = TeacherPaginationService(session)
    mapper = TeacherMapper()

    teacher = teacher_pagination_service.get_teacher_by_email(email=teacher_input.email)

    if teacher :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="There is already an teacher with that email"
        )

    response = teacher_service.create_teacher(teacher=teacher_input)

    return mapper.to_api(response, subjects=teacher_input.list_of_subjects)

@router.delete(
    "/teacher/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_teacher(
    id: str,
    session: Session = Depends(get_db)
) :
    teacher_pagination_service = TeacherPaginationService(session)
    teacher_deletion_service = TeacherDeletionService(session)

    teacher =teacher_pagination_service.get_teacher_by_id(id=id)

    if not teacher :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no teacher with that email"
        )

    teacher_deletion_service.delete_teacher(teacher=teacher)
    
@router.get(
    "/teacher",
    response_model=list | dict,
    status_code=status.HTTP_200_OK
)
@authorize(role=["secretary","teacher", "student"])
async def read_teacher(
    request: Request,
    teachers_by_students = False,
    student_id : str = None,
    sanctions = False,
    technology_classroom = False,
    better_than_eight = False,
    current_user : UserModel = Depends(get_current_user),
    filters: TeacherFilterSchema = Depends(),
    session: Session = Depends(get_db)
) :
    teacher_pagination_service = TeacherPaginationService(session) 
    mapper = TeacherMapper()

    if better_than_eight :
        results = teacher_pagination_service.get_teachers_average_better_than_8()
        return mapper.to_teachers_with_average(results)
    elif teachers_by_students :
        results = teacher_pagination_service.get_teachers_by_students(student_id=student_id)
        return mapper.to_teachers_by_students(results)
    elif technology_classroom :
        results = teacher_pagination_service.get_teachers_by_technological_classroom()
        return mapper.to_teachers_technological_classroom(results)
    elif sanctions :
        results, mean_data = teacher_pagination_service.get_teachers_by_sanctions()
        return mapper.to_teachers_sanctions(results, mean_data)


    teachers, subjects = teacher_pagination_service.get_teachers(filter_params=filters)   

    if not teachers :
        return []

    teachers_mapped = []  
  
    for  teacher, subject in zip(teachers, subjects) :
        teachers_mapped.append(mapper.to_api(teacher, list(subject)))
        
    return teachers_mapped

@router.patch(
    "/teacher/{id}",
    response_model=TeacherModel,
    status_code=status.HTTP_200_OK
)
@authorize(role=["secretary","teacher"])
async def update_teacher(
    request: Request,
    id : str,
    filters: TeacherChangeRequest,
    current_user : UserModel = Depends(get_current_user),
    session: Session = Depends(get_db)
) :
    teacher_pagination_service = TeacherPaginationService(session)
    teacher_update_service = TeacherUpdateService(session)
    teacher_subject_service = TeacherSubjectService(session)
    mapper = TeacherMapper()

    teacher = teacher_pagination_service.get_teacher_by_id(id=id)
    subjects = teacher_subject_service.get_teacher_subjects(id=id)
    teacher_model = mapper.to_api(teacher, subjects)

    if not teacher :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no teacher with that id"
        )
    
    teacher_updated = teacher_update_service.update(changes=filters, teacher=teacher_model)

    return teacher_updated