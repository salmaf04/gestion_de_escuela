from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.note import NoteCreateModel, NoteModel
from sqlalchemy.orm import Session
from backend.application.services.note import NoteCreateService, NotePaginationService, NoteUpdateService
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
    note_service = NoteCreateService()
    mapper = NoteMapper()
    
    response = note_service.create_note(session=session, note=note_input, modified_by=user_id)

    return mapper.to_api(response)

@router.get(
    "/note",
    response_model=list[NoteModel] | list[NoteLessThanFifty] | list,
    status_code=status.HTTP_200_OK
)
async def read_note(
    filters: NoteFilterSchema = Depends(),
    less_than_fifty: bool = False,
    session: Session = Depends(get_db)
) :
    note_pagination_service = NotePaginationService()
    mapper = NoteMapper()

    notes = note_pagination_service.get_note(session=session, filter_params=filters)

    if less_than_fifty :
        notes = note_pagination_service.grade_less_than_fifty(session=session)
        return mapper.to_less_than_fifty(notes)

    if not notes :
        return []
    
    mapped_notes = []

    for note in notes :
        mapped_notes.append(mapper.to_api(note))

    return mapped_notes


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
    update_service = NoteUpdateService()
    pagination_service = NotePaginationService()

    note = pagination_service.get_note_by_id(session= session, id=id)

    if not note : 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no note with that id"
        )
    
    updated_note = update_service.update_note(session=session, note_id=id, modified_by=user_id, new_note=new_note)

    return mapper.to_api(updated_note)