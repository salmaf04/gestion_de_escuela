from sqlalchemy import func
from sqlalchemy.orm import Session
from backend.domain.models.tables import StudentNoteTable
from sqlalchemy import select


def get_student_valoration_average(self, session: Session, student_id: str)  :
    value = select(func.sum(StudentNoteTable.note_value)).where(StudentNoteTable.student_id == student_id)
    note_sum = session.execute(value).scalars().first()
    if note_sum is None :
        return None
    rows = select(func.count(StudentNoteTable.grade)).where(StudentNoteTable.student_id == student_id)
    total_valorations = session.execute(rows).scalars().first()
    return note_sum / total_valorations

def calculate_student_average(session: Session, student_id: str, new_note: int) :
    value = select(func.sum(StudentNoteTable.note_value)).where(StudentNoteTable.student_id == student_id)
    note_sum = session.execute(value).scalars().first()
    
    if note_sum is None :
        return None
    updated_note_sum = note_sum + new_note
    rows = select(func.count(StudentNoteTable.note_value)).where(StudentNoteTable.student_id == student_id)
    total_valorations = session.execute(rows).scalars().first()
    return  updated_note_sum / (total_valorations + 1 )


