from backend.domain.schemas.note import NoteModel
from backend.domain.models.tables import StudentNoteTable


class NoteMapper :

    def to_api(self, note: StudentNoteTable) -> NoteModel :
        return NoteModel(
            id = note.entity_id,
            teacher_id = note.teacher_id,
            student_id = note.student_id,
            subject_id = note.subject_id,
            note_value = note.note_value
        )