from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.units import inch


class PdfExportService :
    def to_pdf(self, filename, data):
        # Configurar el documento con márgenes
        doc = SimpleDocTemplate(filename, pagesize=letter, leftMargin=inch, rightMargin=inch)
        styles = getSampleStyleSheet()
        elements = []

        # Título del informe
        elements.append(Paragraph("Informe de Consulta", styles['Title']))

        # Recorrer los datos y agregarlos al PDF
        for row in data:
            # Convertir cada fila a una cadena JSON
            text = row.json()
            # Usar Paragraph para manejar el ajuste de texto automático                                         
            elements.append(Paragraph(text, styles['BodyText']))

        # Construir el PDF
        doc.build(elements)