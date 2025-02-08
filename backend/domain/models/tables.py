from typing import List
from typing import Optional
from enum import Enum as PyEnum
from sqlalchemy import ForeignKey, Table, and_
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Double
from sqlalchemy import Tuple, ARRAY, Enum
from sqlalchemy import event, select, func, inspect, update
from sqlalchemy.schema import DDL
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm.attributes import get_history
from datetime import datetime, timedelta, timezone

import uuid

class TableName(str, PyEnum):
    """
    Enumeration defining all table names in the database.
    Each value represents a specific table name in the system.
    """
    USER = "user"
    TEACHER = "teacher" 
    DEAN = "dean"
    SUBJECT = "subject"
    STUDENT = "student"
    SECRETARY = "secretary"
    ADMINISTRATOR = "administrator"
    CLASSROOM = "classroom"
    COURSE = "course"
    MEAN = "mean"
    TECHNOLOGICAL_MEAN = "technological_mean"
    TEACHING_MATERIAL = "teaching_material"   
    OTHERS = "others"
    MY_DATE = "my_date"
    MEAN_MAINTENANCE_TABLE="mean_maintenance_table"
    STUDENT_NOTE = "student_note"
    TEACHER_NOTE = "teacher_note"
    ABSENCE = "absence"
    CLASSROOM_REQUEST = "classroom_request"
    TEACHER_SUBJECT = "teacher_subject"
    TEACHER_MEAN = 'teacher_request_mean'
    TEACHER_CLASSROOM = 'teacher_request_classroom'
    SANCTION = "sanction_table"
    VALORATION_PERIOD = "valoration_period"

class Roles(str, PyEnum):
    """
    Enumeration defining available user roles in the system.
    Each role represents a different level of access and permissions.
    """
    ADMIN = "administrator"
    SECRETARY = "secretary"
    TEACHER = "teacher"
    DEAN = "dean"
    STUDENT = "student"

    

class MeanState(str, PyEnum):
    """
    Enumeration defining possible states for resources/means.
    Indicates the current condition of the resource.
    """
    EXCELENT = "excelent" 
    GOOD = "good"
    REGULAR = "regular"
    BAD = "bad"    

class MeanType(str, PyEnum):
    """
    Enumeration defining types of available resources/means.
    Classifies different types of resources that can exist.
    """
    TECHNOLOGICAL = "technological"
    TEACHING_MATERIAL = "teaching_material" 
    OTHERS = "others"


class BaseTable(DeclarativeBase):
    """
    Base class for all system tables.
    Defines a universal unique ID (UUID) as primary key for all tables.
    """
    entity_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


teacher_subject_table = Table(
    TableName.TEACHER_SUBJECT.value,
    BaseTable.metadata,
    Column("teacher_id", ForeignKey("teacher.id" , ondelete='CASCADE'), primary_key=True),
    Column("subject_id", ForeignKey("subject.entity_id", ondelete='CASCADE'), primary_key=True),
)


teacher_request_classroom_table = Table(
    TableName.TEACHER_CLASSROOM.value,
    BaseTable.metadata,
    Column("teacher_id", ForeignKey("teacher.id", ondelete='CASCADE'), primary_key=True),
    Column("classroom_id", ForeignKey("classroom.entity_id", ondelete='CASCADE'), primary_key=True),
)


teacher_request_mean_table = Table(
    TableName.TEACHER_MEAN.value,
    BaseTable.metadata,
    Column("teacher_id", ForeignKey("teacher.id", ondelete='CASCADE'), primary_key=True),
    Column("mean_id", ForeignKey("mean.entity_id", ondelete='CASCADE'), primary_key=True),
)
class UserTable(BaseTable) :
    """
    Base table for all system users.
    Implements polymorphic inheritance for different user types.
    Attributes:
        - name: user's first name
        - lastname: user's last name
        - username: unique username
        - email: unique email address
        - hashed_password: encrypted password
        - roles: list of assigned roles
        - type: user type for polymorphism
    """
    __tablename__ = TableName.USER.value
    
    name = Column(String)
    lastname = Column(String)
    username = Column(String, unique=True)
    email = Column(String, unique =True)
    hashed_password = Column(String)
    roles: Mapped[List[Roles]] = mapped_column(ARRAY(Enum(Roles)), default=[], nullable=True)
    type = Column(String)
    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": "type",
    }


class TeacherTable(UserTable):
    """
    Table for storing teacher information.
    Inherits from UserTable and adds teacher-specific attributes.
    Attributes:
        - specialty: teacher's area of expertise
        - contract_type: type of employment contract
        - experience: years of experience
        - average_valoration: average rating from evaluations
        - salary: teacher's salary
        - less_than_three_valoration: count of ratings below 3
    Relationships:
        - sanctions: list of teacher sanctions
        - mean_request: requested resources
        - classroom_request: requested classrooms
        - student_note_association: grades given to students
        - teacher_note_association: ratings received
        - teacher_subject_association: subjects taught
    """
    __tablename__ = TableName.TEACHER.value
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),ForeignKey(f"{TableName.USER.value}.entity_id"), primary_key=True)
    
    specialty = Column(String)
    contract_type = Column(String)
    experience = Column(Integer)
    average_valoration = Column(Double)
    salary = Column(Double)
    less_than_three_valoration = Column(Integer, default=0)     

    sanctions: Mapped[List["SanctionTable"]] = relationship(back_populates="teacher", cascade="all, delete-orphan")

    mean_request = relationship(
        "MeanTable",
        secondary=teacher_request_mean_table,
        back_populates="teachers"
    )

    classroom_request = relationship(
        "ClassroomTable",
        secondary=teacher_request_classroom_table,
        back_populates="teachers",
        cascade="all, delete"
    )

    student_note_association: Mapped[List["StudentNoteTable"]] = relationship(back_populates="teacher", cascade="all, delete-orphan")
    teacher_note_association: Mapped[List["TeacherNoteTable"]] = relationship(back_populates="teacher", cascade="all, delete-orphan")
    teacher_subject_association = relationship("SubjectTable", secondary=teacher_subject_table, back_populates="teacher_subject_association")


    __mapper_args__ = {
        "polymorphic_identity": "teacher",
    }

      
class DeanTable(TeacherTable):
    """
    Table for storing dean information.
    Inherits from TeacherTable as deans are also teachers with additional responsibilities.
    """
    __tablename__ = TableName.DEAN.value
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),ForeignKey(f"{TableName.TEACHER.value}.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "dean",
    }

class SecretaryTable(UserTable) :
    """
    Table for storing secretary information.
    Inherits from UserTable for basic user functionality.
    """
    __tablename__ = TableName.SECRETARY.value

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),ForeignKey(f"{TableName.USER.value}.entity_id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "secretary",
    }


class AdministratorTable(UserTable) :
    """
    Table for storing administrator information.
    Inherits from UserTable for basic user functionality.
    """
    __tablename__ = TableName.ADMINISTRATOR.value
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),ForeignKey(f"{TableName.USER.value}.entity_id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "administrator",
    }


class StudentTable(UserTable) :
    """
    Table for storing student information.
    Inherits from UserTable and adds student-specific attributes.
    Attributes:
        - age: student's age
        - extra_activities: participation in extra activities
        - average_note: average grade
        - course_id: associated course
    Relationships:
        - course: enrolled course
        - student_note_association: received grades
        - student_absence_association: recorded absences
        - teacher_note_association: teacher evaluations
    """
    __tablename__ = TableName.STUDENT.value

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),ForeignKey(f"{TableName.USER.value}.entity_id"), primary_key=True)
    age = Column(Integer)
    extra_activities = Column(Boolean, nullable=True)
    average_note = Column(Double)
    course_id : Mapped[uuid.UUID] = mapped_column(ForeignKey(f"{TableName.COURSE.value}.entity_id", ondelete='CASCADE'))
   
    course: Mapped['CourseTable'] = relationship(back_populates="students")
    student_note_association: Mapped[List["StudentNoteTable"]] = relationship('StudentNoteTable', back_populates="student", cascade="all, delete-orphan")
    student_absence_association: Mapped[List["AbsenceTable"]] = relationship(back_populates="student", cascade="all, delete-orphan")
    teacher_note_association: Mapped[List["TeacherNoteTable"]] = relationship(back_populates="student")

    __mapper_args__ = {
        "polymorphic_identity": "student",
    }


class SubjectTable(BaseTable) :
    """
    Table for storing subject information.
    Attributes:
        - name: subject name
        - hourly_load: hours per week
        - study_program: program year/level
    Relationships:
        - classroom: assigned classroom
        - course: associated course
        - various associations with students and teachers
    """
    __tablename__ = TableName.SUBJECT.value

    name = Column(String)
    hourly_load  = Column(Integer)
    study_program = Column(Integer)

    classroom_id : Mapped[int] = mapped_column(ForeignKey(f"{TableName.CLASSROOM.value}.entity_id", ondelete='SET NULL'), nullable=True)
    course_id : Mapped[uuid.UUID] = mapped_column(ForeignKey(f"{TableName.COURSE.value}.entity_id"))
  
    classroom: Mapped["ClassroomTable"] = relationship(back_populates="subjects")
    course: Mapped['CourseTable'] = relationship(back_populates="subjects")

    student_teacher_association: Mapped[List["StudentNoteTable"]] = relationship(back_populates="subject", cascade="all, delete-orphan")
    student_absence_association: Mapped[List["AbsenceTable"]] = relationship(back_populates="subject", cascade="all, delete-orphan")
    teacher_note_association: Mapped[List["TeacherNoteTable"]] = relationship(back_populates="subject", cascade="all, delete-orphan")
    teacher_subject_association = relationship("TeacherTable", secondary=teacher_subject_table, back_populates="teacher_subject_association")
    
class ClassroomTable(BaseTable) : 
    """
    Table for storing classroom information.
    Attributes:
        - number: unique classroom number
        - location: physical location
        - capacity: maximum student capacity
    Relationships:
        - teachers: teachers requesting the classroom
        - means: resources in the classroom
        - subjects: subjects taught in the classroom
    """
    __tablename__ = TableName.CLASSROOM.value

    number = Column(Integer, unique=True)
    location = Column(String)
    capacity = Column(Integer)

    teachers = relationship(
        "TeacherTable",
        secondary=teacher_request_classroom_table,
        back_populates="classroom_request",
    )
    means: Mapped[List["MeanTable"]] = relationship(back_populates="classroom")
    subjects : Mapped[List["SubjectTable"]] = relationship(back_populates="classroom")


class CourseTable(BaseTable) :
    __tablename__ = TableName.COURSE.value

    year = Column(Integer, nullable=False, unique=True)

    """
    students: Mapped[List["Student"]] = relationship(
        secondary=f"{TableName.STUDENT.value}", back_populates="course"
    )
    """

    subjects: Mapped[List["SubjectTable"]] = relationship(
        back_populates="course",
        cascade="all, delete-orphan"
    )
    students: Mapped[List["StudentTable"]] = relationship(back_populates="course")
    teacher_note_association: Mapped[List["TeacherNoteTable"]] = relationship(back_populates="course")



class MeanTable(BaseTable) :
    __tablename__ = TableName.MEAN.value
 
    name = Column(String) 
    state: Mapped[MeanState] = mapped_column(String)
    location = Column(String)
    classroom_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),ForeignKey(f"{TableName.CLASSROOM.value}.entity_id", ondelete='SET NULL'), nullable=True)
    to_be_replaced = Column(Boolean, default=False)
    type: Mapped[MeanType] = mapped_column(String)

    mean_maintenance_association: Mapped[List["MeanMaintenanceTable"]] = relationship(back_populates="mean", cascade="all, delete-orphan")

    classroom: Mapped["ClassroomTable"] = relationship(back_populates="means")

    teachers = relationship(
        "TeacherTable",
        secondary=teacher_request_mean_table,
        back_populates="mean_request"
    )


    __mapper_args__ = {
        "polymorphic_identity": "mean",
        "polymorphic_on": "type",
    }


class TechnologicalMeanTable(MeanTable) : 
    __tablename__ = TableName.TECHNOLOGICAL_MEAN.value  

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),ForeignKey(f"{TableName.MEAN.value}.entity_id"), primary_key=True)

    
    __mapper_args__ = {
        "polymorphic_identity": "technological_mean",
    }


class TeachingMaterialTable(MeanTable) : 
    __tablename__ = TableName.TEACHING_MATERIAL.value   

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),ForeignKey(f"{TableName.MEAN.value}.entity_id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "teaching_material",
    }

class OthersTable(MeanTable) : 
    __tablename__ = TableName.OTHERS.value

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),ForeignKey(f"{TableName.MEAN.value}.entity_id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "other",
    }


class MyDateTable(BaseTable):
    __tablename__ = TableName.MY_DATE.value

    date = Column(DateTime, unique= True)

    
class ValorationPeriodTable(BaseTable):
    __tablename__ = TableName.VALORATION_PERIOD.value   
    open = Column(Boolean, default=False)

class StudentNoteTable(BaseTable) :
    __tablename__ = TableName.STUDENT_NOTE.value

    teacher_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.TEACHER.value}.id"))
    student_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.STUDENT.value}.id"), primary_key=True)
    subject_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.SUBJECT.value}.entity_id"), primary_key=True)
    
    last_modified_by: Mapped[int] = mapped_column(ForeignKey(f"{TableName.USER.value}.entity_id"), nullable=False)

    note_value = Column(Integer)    
    
    teacher: Mapped["TeacherTable"] = relationship(back_populates="student_note_association", foreign_keys=[teacher_id])
    student: Mapped["StudentTable"] = relationship(back_populates="student_note_association", foreign_keys=[student_id])
    subject: Mapped["SubjectTable"] = relationship(back_populates="student_teacher_association", foreign_keys=[subject_id])


class TeacherNoteTable(BaseTable) :
    __tablename__ = TableName.TEACHER_NOTE.value

    teacher_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.TEACHER.value}.id"), primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.STUDENT.value}.id", ondelete='SET NULL'), nullable=True)
    subject_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.SUBJECT.value}.entity_id"), primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.COURSE.value}.entity_id"))
    
    grade = Column(Integer)

    teacher: Mapped["TeacherTable"] = relationship(back_populates="teacher_note_association")
    student: Mapped["StudentTable"] = relationship(back_populates="teacher_note_association")
    subject: Mapped["SubjectTable"] = relationship(back_populates="teacher_note_association")
    course: Mapped["CourseTable"] = relationship(back_populates="teacher_note_association")
        
class AbsenceTable(BaseTable) :
    __tablename__ = TableName.ABSENCE.value

    student_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.STUDENT.value}.id"), primary_key=True)
    subject_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.SUBJECT.value}.entity_id"), primary_key=True)

    date = Column(DateTime, nullable=False)

    student: Mapped["StudentTable"] = relationship(back_populates="student_absence_association")
    subject: Mapped["SubjectTable"] = relationship(back_populates="student_absence_association")


#Tablas de relación
class MeanMaintenanceTable(BaseTable) :
    __tablename__ = TableName.MEAN_MAINTENANCE_TABLE.value

    mean_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.MEAN.value}.entity_id"), primary_key= True)
    finished = Column(Boolean, default=False)

    cost = Column(Double)

    mean: Mapped["MeanTable"] = relationship(back_populates="mean_maintenance_association")
    date = Column(DateTime, nullable=False)


class SanctionTable(BaseTable):
    __tablename__ = TableName.SANCTION.value

    teacher_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.TEACHER.value}.id"), nullable=False)
    teacher: Mapped["TeacherTable"] = relationship(back_populates="sanctions")
    amount: Mapped[Double] = mapped_column(Double, nullable=False)
    date = Column(DateTime, nullable=False)


@event.listens_for(TeacherNoteTable, 'after_insert')
def update_teacher_average(mapper, connection, target):
    """
    Updates teacher's average rating after a new evaluation is inserted.
    Calculates the average of all grades for the teacher.
    """
    connection.execute(
        TeacherTable.__table__.update().
        where(TeacherTable.id == target.teacher_id).
        values(average_valoration=(
            select((func.sum(TeacherNoteTable.grade)/func.count())).
            where(TeacherNoteTable.teacher_id == target.teacher_id)
        ))
    )

def update_student_average(mapper, connection, target):
    """
    Updates student's average grade after a new grade is added or modified.
    Calculates the average of all grades for the student.
    """
    connection.execute(
        StudentTable.__table__.update().
        where(StudentTable.id == target.student_id).
        values(average_note=(
            select((func.sum(StudentNoteTable.note_value)/func.count())).
            where(StudentNoteTable.student_id == target.student_id)
        ))
    )

event.listen(StudentNoteTable, 'after_insert', update_student_average)
event.listen(StudentNoteTable, 'after_update', update_student_average)

@event.listens_for(BaseTable.metadata, 'after_create')
def insert_default_valoration_period(target, connection, **kw):
    """
    Creates a default evaluation period when the database is initialized.
    Checks if ValorationPeriodTable exists and is empty before inserting.
    """
    for table in target.tables.values():
        if table.name == ValorationPeriodTable.__tablename__:  
            result = connection.execute(select(ValorationPeriodTable.entity_id)).fetchone()
            
            if result is None:
                connection.execute(
                    ValorationPeriodTable.__table__.insert().
                    values(
                        entity_id=uuid.uuid4(),
                        open=False
                    )
                )
            break
 
@event.listens_for(ValorationPeriodTable, 'after_update', propagate=True)
def update_less_than_three_valoration(mapper, connection, target):
    history = get_history(target, 'open')
    unchanged = history.unchanged[0] if history.unchanged else None
    old_value = history.deleted[0] if history.deleted else None
    new_value = history.added[0] if history.added else None


    if not unchanged :
        if old_value == True and new_value == False :
    # Actualizar el promedio de valoraciones del profesor
            connection.execute(
                TeacherTable.__table__.update().
                where(TeacherTable.average_valoration < 3).
                values(less_than_three_valoration= TeacherTable.less_than_three_valoration + 1)
                )
            
def insert_user_roles(mapper, connection, target):
    """
    Assigns appropriate roles to users based on their type during insertion.
    Maps user types to corresponding role enums.
    """
    if target.type == "administrator" :
        target.roles = [Roles.ADMIN.value]
    elif target.type == "secretary" :
        target.roles = [Roles.SECRETARY.value]
    elif target.type == "teacher" :
        target.roles = [Roles.TEACHER.value]
    elif target.type == "student" :
        target.roles = [Roles.STUDENT.value]

for table in [TeacherTable, UserTable, AdministratorTable, SecretaryTable, StudentTable] :
    event.listen(table, 'before_insert', insert_user_roles)


@event.listens_for(DeanTable, 'before_insert')
def no_administrator(mapper, connection, target):
    """
    Manages dean roles and admin privileges during dean insertion.
    Assigns admin role to dean if no administrator exists.
    """
    result = connection.execute(select(AdministratorTable.entity_id)).fetchone()
    if result is None :
        target.roles = [Roles.DEAN.value, Roles.TEACHER.value, Roles.ADMIN.value]
    else :
        target.roles = [Roles.DEAN.value, Roles.TEACHER.value]

@event.listens_for(AdministratorTable, 'after_delete')
def check_administrator(mapper, connection, target):
    """
    Manages admin privileges after administrator deletion.
    Transfers admin role to dean if no administrator remains.
    """
    result = connection.execute(select(AdministratorTable.entity_id)).fetchone()
    decano = connection.execute(select(DeanTable)).fetchone()
    if result is None :
        connection.execute(UserTable.__table__.update().values(roles=[Roles.DEAN.value, Roles.TEACHER.value, Roles.ADMIN.value]).where(UserTable.entity_id == decano.id))

@event.listens_for(AdministratorTable, 'before_insert')
def check_administrator(mapper, connection, target):
    """
    Manages admin privileges before administrator insertion.
    Adjusts dean roles when new administrator is added.
    """
    result = connection.execute(select(AdministratorTable.entity_id)).fetchone()
    decano = connection.execute(select(DeanTable)).fetchone()
    if result is None :
        connection.execute(UserTable.__table__.update().values(roles=[Roles.DEAN.value, Roles.TEACHER.value]).where(UserTable.entity_id == decano.id))

@event.listens_for(DeanTable, 'after_delete')
def check_dean(mapper, connection, target):
    """
    Manages dean privileges after dean deletion.
    Transfers admin role to administrator if no dean remains.
    """
    user_id = target.id
    print(user_id)
    print('hola')
    connection.execute(UserTable.__table__.update().values(roles=[Roles.TEACHER.value]).where(UserTable.entity_id == user_id))

@event.listens_for(MeanMaintenanceTable, 'before_insert')
def check_replacement(mapper, connection, target):
    """
    Checks if a resource needs replacement based on maintenance history.
    Flags resource for replacement if it has had 2+ maintenance records in the past year.
    """
    date = datetime.now(timezone.utc) - timedelta(days=365)
    result = connection.execute(
        select(
            func.count(MeanMaintenanceTable.entity_id).label("count")
        ).where(
            and_(
                MeanMaintenanceTable.date >= date,
                MeanMaintenanceTable.mean_id == target.mean_id
            )
        )
    ).scalars().first()

    if result >= 2 : 
        connection.execute(update(MeanTable).where(MeanTable.entity_id == target.mean_id).values(to_be_replaced=True))
    
