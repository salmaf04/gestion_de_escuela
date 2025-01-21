from sqlalchemy.orm import Session
from backend.domain.schemas.note import NoteCreateModel
from backend.domain.models.tables import StudentNoteTable, StudentTable, TeacherTable
from backend.application.services.student import StudentPaginationService
from backend.application.services.subject import SubjectPaginationService
from backend.application.services.teacher import TeacherPaginationService
from backend.domain.filters.note import NoteFilterSet , NoteFilterSchema
from sqlalchemy import select, func, update
from backend.application.services.student import UpdateNoteAverageService
class NoteCreateService :
    def create_note(self, session: Session, note: NoteCreateModel, modified_by : str) -> StudentNoteTable :
        update_note_average_service = UpdateNoteAverageService()
        update_note_average_service.update_note_average(session=session, student_id=note.student_id, new_note=note.note_value)

        note_dict = note.model_dump()
        new_note = StudentNoteTable(**note_dict, last_modified_by = modified_by)
        
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
    def get_note_by_id(self, session: Session, id : str) -> StudentNoteTable :
        query = select(StudentNoteTable).where(StudentNoteTable.entity_id == id)
        return session.execute(query).scalars().first()

    def get_note(self, session: Session, filter_params: NoteFilterSchema) -> list[StudentNoteTable] :
        query = select(StudentNoteTable)
        filter_set = NoteFilterSet(session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return session.execute(query).scalars().all()
    
    def grade_less_than_fifty(self, session: Session) :
        query = select(StudentNoteTable.student_id, StudentNoteTable.subject_id, (func.sum(StudentNoteTable.note_value)/func.count()).label('average_note'))
        query = query.group_by(StudentNoteTable.student_id, StudentNoteTable.subject_id)
        query = query.having((func.sum(StudentNoteTable.note_value)/func.count()) < 50)

        query = query.subquery()

        second_query = select(query.c.student_id)
        second_query = second_query.group_by(query.c.student_id)
        second_query = second_query.having((func.count(query.c.student_id)) > 1).subquery()

        combined_query = (
        select(
            StudentTable.name.label('student_name'),
            StudentTable.id.label('student_id'),
            TeacherTable.name.label('teacher_name'),
            func.avg(TeacherTable.average_valoration).label('average_teacher_valoration')
        )
        .join(second_query, second_query.c.student_id == StudentTable.id)
        .join(StudentNoteTable, StudentNoteTable.student_id == StudentTable.id)
        .join(TeacherTable, TeacherTable.id == StudentNoteTable.teacher_id)
        .group_by(StudentTable.name, StudentTable.id, TeacherTable.name)
        )

    # Ejecutar la consulta
        results = session.execute(combined_query).fetchall()

        return results
       
        """
        final_query = select(StudentTable.name, second_query.c.student_id)
        final_query = final_query.join(second_query, StudentTable.entity_id == second_query.c.student_id)
        final_query = final_query.group_by(StudentTable.name, second_query.c.student_id)
        """


class NoteUpdateService() :
    def update_note(self, session: Session, note_id : str , modified_by : str, new_note : float ) :
        pagination_service = NotePaginationService()
        update_statement = update(StudentNoteTable).where(StudentNoteTable.entity_id == note_id).values(note_value = new_note, last_modified_by = modified_by)
        session.execute(update_statement)
        session.commit()

        return pagination_service.get_note_by_id(session=session, id=note_id)

    




       