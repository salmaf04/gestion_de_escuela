from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.note import NoteCreateModel, NoteModel
from sqlalchemy.orm import Session
from backend.application.services.note import NoteCreateService
from backend.application.serializers.note import NoteMapper
from backend.configuration import get_db

router = APIRouter()

@router.post(
    "/note",
    response_model=NoteModel,
    status_code=status.HTTP_201_CREATED
) 
async def create_note(
    note_input: NoteCreateModel,
    session: Session = Depends(get_db)
) :
    note_service = NoteCreateService()
    mapper = NoteMapper()

    response = note_service.create_note(session=session, note=note_input)

    return mapper.to_api(response)