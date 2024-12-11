from backend.domain.schemas.note import NoteModel
from backend.domain.models.tables import StudentNoteTable


class NoteMapper :

    def to_api(self, note: StudentNoteTable) -> NoteModel :
        return NoteModel(
            id = note.entity_id,
            teacher = note.teacher.name,
            student = note.student.name,
            subject = note.subject.name,
            note_value = note.note_value
        )