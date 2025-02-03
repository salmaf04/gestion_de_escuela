from sqlalchemy.orm import Session
from backend.domain.schemas.note import NoteCreateModel
from backend.domain.models.tables import StudentNoteTable, StudentTable, TeacherTable, SubjectTable
from backend.application.services.student import StudentPaginationService
from backend.application.services.subject import SubjectPaginationService
from backend.application.services.teacher import TeacherPaginationService
from backend.domain.filters.note import NoteFilterSet , NoteFilterSchema, NoteChangeRequest
from sqlalchemy import select, func, update
from backend.application.services.student import UpdateNoteAverageService
from .base import IRepository

class NoteRepository(IRepository[NoteCreateModel,StudentNoteTable, NoteChangeRequest,NoteFilterSchema]):
    def __init__(self, session):
        super().__init__(session)

    def create(self, note: NoteCreateModel, modified_by : str, student: StudentTable, subject: SubjectTable, teacher: TeacherTable) -> StudentNoteTable :
        note_dict = note.model_dump()
        new_note = StudentNoteTable(**note_dict, last_modified_by = modified_by)
        
        new_note.student = student
        new_note.subject = subject  
        new_note.teacher = teacher

        teacher.student_note_association.append(new_note)
        subject.student_teacher_association.append(new_note)
        student.student_note_association.append(new_note)

        self.session.add(new_note)
        self.session.commit()
        return new_note

    def delete(self, entity: StudentNoteTable) -> None :
        self.session.delete(entity)
        self.session.commit()

    def update(self, changes : NoteChangeRequest , entity : StudentNoteTable, modified_by : str) -> StudentNoteTable :
        entity.note_value = changes.note_value
        self.session.commit()
        return self.get_by_id(id=entity.entity_id)

    def get_by_id(self, id: str ) -> StudentNoteTable :
        query = self.session.query(StudentNoteTable).filter(StudentNoteTable.entity_id == id)

        result = query.scalar()

        return result

    def get(self, filter_params: NoteFilterSchema) -> list[StudentNoteTable] :
        query = select(StudentNoteTable)
        filter_set = NoteFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return self.session.execute(query).scalars().all()

    def grade_less_than_fifty(self) :
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
        results = self.session.execute(combined_query).fetchall()
        return results
       
    