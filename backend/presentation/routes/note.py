from fastapi import APIRouter, HTTPException, status, Depends
from backend.domain.schemas.note import NoteCreateModel, NoteModel
from sqlalchemy.orm import Session
from backend.application.services.note import NoteCreateService, NotePaginationService
from backend.application.serializers.note import NoteMapper
from backend.configuration import get_db
from backend.domain.filters.note import NoteFilterSchema
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import json
from backend.application.serializers.note import NoteLessThanFifty

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

@router.get(
    "/note",
    response_model=list[NoteModel] | list[NoteLessThanFifty],
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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no note with that fields"
        )

    notes_mapped = {}    
     
    for i, note in enumerate(notes) :
        notes_mapped[i] = mapper.to_api(note)
        
    return notes_mapped