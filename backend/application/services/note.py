from sqlalchemy.orm import Session
from backend.domain.schemas.note import NoteCreateModel
from backend.domain.models.tables import StudentNoteTable
from backend.application.services.student import StudentPaginationService
from backend.application.services.subject import SubjectPaginationService
from backend.application.services.teacher import TeacherPaginationService

class NoteCreateService :
    def create_note(self, session: Session, note: NoteCreateModel) -> StudentNoteTable :
        note_dict = note.model_dump()
        new_note = StudentNoteTable(**note_dict)
        
        student = StudentPaginationService().get_student_by_id(session=session, id=note.student_id)
        subject = SubjectPaginationService().get_subject_by_id(session=session, id=note.subject_id)
        teacher = TeacherPaginationService().get_teacher_by_id(session=session, id=note.teacher_id)

        new_note.student = student
        new_note.subject = subject  
        new_note.teacher = teacher

        teacher.student_note_association.append(new_note)
        subject.student_teacher_association.append(new_note)
        student.student_note_association.append(new_note)

        session.add(new_note)
        session.commit()
        return new_note