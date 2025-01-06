from backend.domain.schemas.note import NoteModel
from backend.domain.models.tables import StudentNoteTable
from pydantic import BaseModel
import uuid
from backend.application.services.student import StudentPaginationService

class NoteLessThanFifty(BaseModel) :
    id : uuid.UUID
    name : str
    note : float
    teachers : dict

class NoteMapper :
    def to_api(self, note: StudentNoteTable) -> NoteModel :
        return NoteModel(
            id = note.entity_id,
            teacher = note.teacher.name,
            student = note.student.name,
            subject = note.subject.name,
            note_value = note.note_value
        )
    
    def to_less_than_fifty(self, data) :
        serialized_values = []

        for response in data[0] :
            teachers_with_average = {}

            for relation_list in data[1] :
                for relation in relation_list :
                    if relation.teacher.name not in teachers_with_average :
                        teachers_with_average[relation.teacher.name] = relation.teacher.average_valoration
                    else :
                        continue
                    
            note = NoteLessThanFifty(
                name= response.name,
                id = response.id,
                note = response.average_note,
                teachers= teachers_with_average
            )
            serialized_values.append(note)

        return list(serialized_values)


