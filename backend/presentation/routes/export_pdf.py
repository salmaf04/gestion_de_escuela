from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from backend.application.services.pdf_export import PdfExportService
from backend.configuration import get_db
from pydantic import BaseModel

router = APIRouter()

@router.post(
    "/export_pdf",
    status_code=status.HTTP_201_CREATED
)
async def export_pdf(
    to_export: BaseModel,
    session: Session = Depends(get_db)
) :
    export_pdf_service = PdfExportService()

    export_pdf_service.export_pdf(session=session, to_export=to_export)

    return {"message": "PDF Exportado"}