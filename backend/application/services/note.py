from sqlalchemy.orm import Session
from backend.domain.schemas.note import NoteCreateModel
from backend.domain.models.tables import StudentNoteTable, StudentTable
from backend.application.services.student import StudentPaginationService
from backend.application.services.subject import SubjectPaginationService
from backend.application.services.teacher import TeacherPaginationService
from backend.domain.filters.note import NoteFilterSet , NoteFilterSchema
from sqlalchemy import select
from backend.application.services.student import UpdateNoteAverageService
class NoteCreateService :
    def create_note(self, session: Session, note: NoteCreateModel) -> StudentNoteTable :
        update_note_average_service = UpdateNoteAverageService()
        update_note_average_service.update_note_average(session=session, student_id=note.student_id, new_note=note.note_value)

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
    
class NotePaginationService :
    def get_note(self, session: Session, filter_params: NoteFilterSchema) -> list[StudentNoteTable] :
        query = select(StudentNoteTable)
        filter_set = NoteFilterSet(session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return session.execute(query).scalars().all()
    
    def grade_less_than_fifty(self, session: Session) :
        student_note_association = []
        pagination_service = StudentPaginationService()
        query = select(StudentTable.id , StudentTable.name, StudentTable.average_note)
        query = query.where(StudentTable.average_note < 50)
        
        results = session.execute(query).all()

        for student in results :
            student = pagination_service.get_student_by_id(session=session, id=student.id)
            student_note_association.append(student.student_note_association)

        return results, student_note_association