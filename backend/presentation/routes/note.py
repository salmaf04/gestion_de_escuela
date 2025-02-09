from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.note import NoteCreateModel, NoteModel
from sqlalchemy.orm import Session
from backend.application.services.note import NoteCreateService, NotePaginationService, NoteUpdateService, NoteDeleteService
from backend.application.serializers.note import NoteMapper
from backend.configuration import get_db
from backend.domain.filters.note import NoteFilterSchema, NoteChangeRequest
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import json
from backend.application.serializers.note import NoteLessThanFifty
from backend.domain.schemas.user import UserModel
from backend.presentation.utils.auth import authorize
from backend.presentation.utils.auth import get_current_user
import uuid
from fastapi.security import OAuth2PasswordBearer
from fastapi import Request

"""
This module defines API endpoints for managing notes using FastAPI.

Endpoints:
- POST /note: Create a new note. Requires authorization for roles 'secretary' or 'teacher'.
- GET /note: Retrieve a list of notes based on filters, including options for notes by student or notes with grades less than fifty. Requires authorization for roles 'secretary', 'teacher', or 'student'.
- PATCH /note/{id}: Update an existing note by its ID. Requires authorization for roles 'secretary' or 'teacher'.

Dependencies:
- FastAPI's APIRouter for routing.
- SQLAlchemy's Session for database interactions.
- Custom services and models for handling note operations.
- OAuth2PasswordBearer for token-based authentication.

Functions:
- create_note: Handles the creation of a new note. Utilizes the NoteCreateService to add a note to the database.
- read_note: Retrieves notes based on filter criteria, including options for notes by student or notes with grades less than fifty.
- update_note: Updates an existing note. Validates the existence of the note and applies changes if valid.

Parameters:
- note_input (NoteCreateModel): The data for creating a new note.
- by_student (str): The ID of the student to filter notes by.
- less_than_fifty (bool): Indicates if the user wants to retrieve notes with grades less than fifty.
- id (str): The ID of the note to update.
- new_note (NoteChangeRequest): The changes to apply to the note.
- session (Session): The database session dependency.
- current_user (UserModel): The current authenticated user.

Returns:
- JSON responses with the created, retrieved, or updated note records.

Raises:
- HTTPException: Raised when a note is not found, with appropriate HTTP status codes.
"""

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

@router.post(
    "/note",
    response_model=NoteModel,
    status_code=status.HTTP_201_CREATED
) 
@authorize(role=['secretary','teacher'])
async def create_note(
    request: Request,
    note_input: NoteCreateModel,
    session: Session = Depends(get_db),
    user_id : str = None,
    current_user: UserModel = Depends(get_current_user),    
) :
    note_service = NoteCreateService(session)
    mapper = NoteMapper()
    
    response = note_service.create_note(note=note_input, modified_by=user_id)

    return mapper.to_post(response)

@router.get(
    "/note",
    response_model=list[NoteModel] | list[NoteLessThanFifty] | list,
    status_code=status.HTTP_200_OK
)
@authorize(role=['secretary','teacher', 'student'])
async def read_note(
    request: Request,
    by_student : str = None,
    by_teacher : str = None,
    filters: NoteFilterSchema = Depends(),
    less_than_fifty: bool = False,
    session: Session = Depends(get_db),
    current_user : UserModel = Depends(get_current_user)
) :
    note_pagination_service = NotePaginationService(session)
    mapper = NoteMapper()

    if less_than_fifty :
        notes = note_pagination_service.grade_less_than_fifty()
        return mapper.to_less_than_fifty(notes)
    elif by_student :
        notes = note_pagination_service.get_note_by_student(student_id=by_student)
    elif by_teacher :
        notes = note_pagination_service.get_note_by_student_by_teacher(teacher_id=by_teacher)
        print(len(notes))
        return mapper.to_note_by_teacher(notes)
    else :
        notes = note_pagination_service.get_note(filter_params=filters)

    if not notes :
        return []
    
    return mapper.to_api(notes)


@router.patch(
    "/note/{id}",
    status_code=status.HTTP_200_OK,
    response_model=NoteModel,
    responses={ 
        status.HTTP_404_NOT_FOUND: {
            "description": "Not found",
        }
    },
) 
@authorize(role=['secretary','teacher'])
async def update_note(
    id: str,
    new_note: NoteChangeRequest,
    request: Request,
    current_user: UserModel = Depends(get_current_user),
    user_id : str = None,
    session: Session = Depends(get_db),
) :
    mapper = NoteMapper()
    update_service = NoteUpdateService(session)
    pagination_service = NotePaginationService(session)
    
    note = pagination_service.get_note_by_id(id=id)

    if not note : 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no note with that id"
        )
    
    updated_note = update_service.update_note(note=note, modified_by=user_id, new_note=new_note)

    return mapper.to_api(updated_note)

@router.delete(
    "/note/{id}",
    status_code=status.HTTP_200_OK
) 
async def delete_note(
    id: str,
    session: Session = Depends(get_db)
) :
    note_pagination_service = NotePaginationService(session)
    note_delete_service = NoteDeleteService(session)
    note = note_pagination_service.get_note_by_id(id=id)

    if not note : 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no note with that id"
        )
    
    note_delete_service.delete(note=note)