from sqlalchemy import func
from sqlalchemy.orm import Session
from backend.domain.models.tables import TeacherNoteTable
from sqlalchemy import select


def get_teacher_valoration_average(self, session: Session, teacher_id: str)  :
    value = select(func.sum(TeacherNoteTable.grade)).where(TeacherNoteTable.teacher_id == teacher_id)
    note_sum = session.execute(value).scalars().first()
    if note_sum is None :
        return None
    rows = select(func.count(TeacherNoteTable.grade)).where(TeacherNoteTable.teacher_id == teacher_id)
    total_valorations = session.execute(rows).scalars().first()
    return note_sum / total_valorations

def calculate_teacher_average(session: Session, teacher_id: str, new_note: int) :
    value = select(func.sum(TeacherNoteTable.grade)).where(TeacherNoteTable.teacher_id == teacher_id)
    note_sum = session.execute(value).scalars().first()
    
    if note_sum is None :
        return None
    updated_note_sum = note_sum + new_note
    rows = select(func.count(TeacherNoteTable.grade)).where(TeacherNoteTable.teacher_id == teacher_id)
    total_valorations = session.execute(rows).scalars().first()
    return  updated_note_sum / (total_valorations + 1 )

