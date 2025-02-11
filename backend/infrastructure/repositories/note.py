from sqlalchemy.orm import Session
from backend.domain.schemas.note import NoteCreateModel
from backend.domain.models.tables import StudentNoteTable, StudentTable, TeacherTable, SubjectTable, teacher_subject_table, CourseTable, UserTable
from backend.application.services.student import StudentPaginationService
from backend.application.services.subject import SubjectPaginationService
from backend.application.services.teacher import TeacherPaginationService
from backend.domain.filters.note import NoteFilterSet , NoteFilterSchema, NoteChangeRequest
from sqlalchemy import select, func, update, and_
from sqlalchemy.orm import aliased
from backend.application.services.student import UpdateNoteAverageService
from .base import IRepository

class NoteRepository(IRepository[NoteCreateModel,StudentNoteTable, NoteChangeRequest,NoteFilterSchema]):
    """
    Repository for managing student notes/grades in the database.
    Extends IRepository with specific implementations for grade operations.
    """
    def __init__(self, session):
        """Initialize repository with database session."""
        super().__init__(session)

    def create(self, note: NoteCreateModel, modified_by: str, student: StudentTable, subject: SubjectTable, teacher: TeacherTable) -> StudentNoteTable:
        """
        Create a new student note record with associations to student, subject, and teacher.
        Args:
            note: NoteCreateModel containing note details
            modified_by: String identifier of who created the note
            student: StudentTable instance the note belongs to
            subject: SubjectTable instance the note is for
            teacher: TeacherTable instance who gave the note
        Returns:
            Created StudentNoteTable instance
        """
        note_dict = note.model_dump()
        new_note = StudentNoteTable(**note_dict, last_modified_by=modified_by)
        
        # Establecer relaciones
        new_note.student = student
        new_note.subject = subject  
        new_note.teacher = teacher

        # Agregar asociaciones
        teacher.student_note_association.append(new_note)
        subject.student_teacher_association.append(new_note)
        student.student_note_association.append(new_note)

        self.session.add(new_note)
        self.session.commit()
        return new_note

    def delete(self, entity: StudentNoteTable) -> None:
        """Delete a student note from the database."""
        self.session.delete(entity)
        self.session.commit()

    def update(self, changes: NoteChangeRequest, entity: StudentNoteTable, modified_by: str) -> StudentNoteTable:
        """
        Update a student note's value.
        Args:
            changes: NoteChangeRequest containing new note value
            entity: StudentNoteTable to be updated
            modified_by: String identifier of who modified the note
        Returns:
            Updated StudentNoteTable instance
        """
        entity.note_value = changes.note_value
        self.session.commit()
        
        update_stmt = update(StudentNoteTable).where(StudentNoteTable.entity_id == entity.entity_id).values(last_modified_by=modified_by)
        self.session.execute(update_stmt)
        self.session.commit()

        new_note = self.get(
            NoteFilterSchema(id=entity.entity_id)
        )

        return new_note

    def get_by_id(self, id: str) -> StudentNoteTable:
        """Retrieve a note by its ID."""
        query = self.session.query(StudentNoteTable).filter(StudentNoteTable.entity_id == id)
        result = query.scalar()
        return result

    def get(self, filter_params: NoteFilterSchema) -> list[StudentNoteTable]:
        """Get notes based on filter parameters."""
        
        user_alias = aliased(UserTable)
        
        query = select(StudentNoteTable, StudentTable, TeacherTable, SubjectTable, CourseTable , user_alias)
        query = query.join(StudentTable, StudentNoteTable.student_id == StudentTable.entity_id)
        query = query.join(CourseTable, StudentTable.course_id == CourseTable.entity_id)
        query = query.join(TeacherTable, StudentNoteTable.teacher_id == TeacherTable.entity_id)
        query = query.join(SubjectTable, StudentNoteTable.subject_id == SubjectTable.entity_id)
        query = query.join(user_alias, StudentNoteTable.last_modified_by == user_alias.entity_id)
        query = query.order_by(StudentNoteTable.entity_id)

        filter_set = NoteFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True)) 
        return self.session.execute(query).all()

    def grade_less_than_fifty(self):
        """
        Get students with average grades less than 50 in more than one subject.
        Returns information about students and their teachers.
        Returns:
            List of tuples containing student and teacher information
        """
        # Subconsulta para obtener promedios por estudiante y asignatura
        query = select(StudentNoteTable.student_id, StudentNoteTable.subject_id, 
                      (func.sum(StudentNoteTable.note_value)/func.count()).label('average_note'))
        query = query.group_by(StudentNoteTable.student_id, StudentNoteTable.subject_id)
        query = query.having((func.sum(StudentNoteTable.note_value)/func.count()) < 50)
        query = query.subquery()

        # Subconsulta para estudiantes con más de una asignatura con promedio bajo
        second_query = select(query.c.student_id)
        second_query = second_query.group_by(query.c.student_id)
        second_query = second_query.having((func.count(query.c.student_id)) > 1).subquery()

        # Final consult to get details
        combined_query = (
            select(
                StudentTable.name.label('student_name'),
                StudentTable.id.label('student_id'),
                TeacherTable.name.label('teacher_name'),
                TeacherTable.average_valoration.label('average_teacher_valoration'),
                TeacherTable.id,
                query.c.subject_id
            )
            .join(second_query, second_query.c.student_id == StudentTable.id)
            .join(query, query.c.student_id == StudentTable.id)
            .join(StudentNoteTable, StudentNoteTable.student_id == StudentTable.id)
            .join(TeacherTable, TeacherTable.id == StudentNoteTable.teacher_id)
            .where(StudentNoteTable.subject_id == query.c.subject_id)
            .distinct(TeacherTable.id, StudentTable.id)
            .order_by(StudentTable.id, TeacherTable.id)
        )
          
        results = self.session.execute(combined_query).all()
        print(results)
        return results
    
    def get_note_by_student(self, student_id: str) -> list[StudentNoteTable]:
        """
        Get all notes for a specific student, ordered by subject.
        Args:
            student_id: ID of the student
        Returns:
            List of StudentNoteTable instances
        """

        user_alias = aliased(UserTable)

        query = select(StudentNoteTable, StudentTable, TeacherTable, SubjectTable, CourseTable, user_alias)
        query = query.join(StudentTable, StudentNoteTable.student_id == StudentTable.entity_id)
        query = query.join(TeacherTable, StudentNoteTable.teacher_id == TeacherTable.entity_id)
        query = query.join(SubjectTable, StudentNoteTable.subject_id == SubjectTable.entity_id)
        query = query.join(CourseTable, StudentTable.course_id == CourseTable.entity_id)
        query = query.join(user_alias, StudentNoteTable.last_modified_by == user_alias.entity_id)
        query = query.where(StudentNoteTable.student_id == student_id)
        query = query.order_by(StudentNoteTable.entity_id)
        return self.session.execute(query).all()
    
    def get_note_by_student_by_teacher(self, teacher_id: str):
        user_alias = aliased(UserTable)

        sub_query = select(teacher_subject_table.c.subject_id)
        sub_query = sub_query.where(teacher_subject_table.c.teacher_id == teacher_id)
        sub_query = sub_query.subquery()

        query = select(StudentNoteTable, StudentTable, TeacherTable, SubjectTable,sub_query.c.subject_id, CourseTable, user_alias)
        query = query.join(StudentTable, StudentNoteTable.student_id == StudentTable.entity_id)
        query = query.join(TeacherTable, StudentNoteTable.teacher_id == TeacherTable.entity_id)
        query = query.join(SubjectTable, StudentNoteTable.subject_id == SubjectTable.entity_id)
        query = query.join(sub_query, StudentNoteTable.subject_id == sub_query.c.subject_id)
        query = query.join(CourseTable, StudentTable.course_id == CourseTable.entity_id)
        query = query.join(user_alias, StudentNoteTable.last_modified_by == user_alias.entity_id)
        query = query.where(
            StudentNoteTable.subject_id.in_(
                select(
                    sub_query.c.subject_id
                )
            )
        )
        query = query.order_by(StudentNoteTable.entity_id)
        return self.session.execute(query).all()
       
    