from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from backend.application.services.pdf_export import PdfExportService
from backend.configuration import get_db
from pydantic import BaseModel

"""
This module defines an API endpoint for exporting data to a PDF using FastAPI.

Endpoint:
- POST /export_pdf: Exports the provided data to a PDF file.

Dependencies:
- FastAPI's APIRouter for routing.
- SQLAlchemy's Session for database interactions.
- PdfExportService for handling the PDF export functionality.

Function:
- export_pdf: Handles the export of data to a PDF. Utilizes the PdfExportService to perform the export operation.

Parameters:
- to_export (BaseModel): The data to be exported to a PDF.
- session (Session): The database session dependency.

Returns:
- A JSON response with a message indicating the success of the PDF export.

Raises:
- HTTPException: Can be raised if there are issues during the export process, with appropriate HTTP status codes.
"""

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