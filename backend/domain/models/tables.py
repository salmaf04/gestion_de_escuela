from typing import List
from typing import Optional
from enum import Enum
from sqlalchemy import ForeignKey, Table
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Double
from sqlalchemy import Tuple
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

import uuid

class TableName(str, Enum):
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
    

class MeanState(str, Enum):
    EXCELENT = "excelent" 
    GOOD = "good"
    REGULAR = "regular"
    BAD = "bad"    

class MeanType(str, Enum) :
    TECHNOLOGICAL = "technological"
    TEACHING_MATERIAL = "teaching_material" 
    OTHERS = "others"


class BaseTable(DeclarativeBase):
    entity_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


teacher_subject_table = Table(
    TableName.TEACHER_SUBJECT.value,
    BaseTable.metadata,
    Column("teacher_id", ForeignKey("teacher.id"), primary_key=True),
    Column("subject_id", ForeignKey("subject.entity_id"), primary_key=True),
)


teacher_request_classroom_table = Table(
    TableName.TEACHER_CLASSROOM.value,
    BaseTable.metadata,
    Column("teacher_id", ForeignKey("teacher.id"), primary_key=True),
    Column("classroom_id", ForeignKey("classroom.entity_id"), primary_key=True),
)


teacher_request_mean_table = Table(
    TableName.TEACHER_MEAN.value,
    BaseTable.metadata,
    Column("teacher_id", ForeignKey("teacher.id"), primary_key=True),
    Column("mean_id", ForeignKey("mean.entity_id"), primary_key=True),
)

class UserTable(BaseTable) :
    __tablename__ = TableName.USER.value
    
    username = Column(String, unique=True)
    email = Column(String, unique =True)
    hash_password = Column(String)
    type = Column(String)
    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": "type",
    }


class TeacherTable(UserTable):
    __tablename__ = TableName.TEACHER.value
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),ForeignKey(f"{TableName.USER.value}.entity_id"), primary_key=True)
    name = Column(String)
    fullname = Column(String)
    specialty = Column(String)
    contract_type = Column(String)
    experience = Column(Integer)
    average_valoration = Column(Double)
    salary = Column(Double)
    """
    students: Mapped[List["Student"]] = relationship(
        secondary=f"{TableName.STUDENT.value}", back_populates="teacher", viewonly=True
    )
    subjects: Mapped[List["Subject"]] = relationship(
        secondary=f"{TableName.SUBJECT.value}", back_populates="teacher", viewonly=True
    )
    """
    
    sanctions: Mapped[List["SanctionTable"]] = relationship(back_populates="teacher")

    mean_request = relationship(
        "MeanTable",
        secondary=teacher_request_mean_table,
        back_populates="teachers",
    )

    classroom_request = relationship(
        "ClassroomTable",
        secondary=teacher_request_classroom_table,
        back_populates="teachers",
    )

    student_note_association: Mapped[List["StudentNoteTable"]] = relationship(back_populates="teacher")
    teacher_note_association: Mapped[List["TeacherNoteTable"]] = relationship(back_populates="teacher")
    teacher_subject_association = relationship("SubjectTable", secondary=teacher_subject_table, back_populates="teacher_subject_association")


    __mapper_args__ = {
        "polymorphic_identity": "teacher",
    }

      
class DeanTable(TeacherTable):
    __tablename__ = TableName.DEAN.value
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),ForeignKey(f"{TableName.TEACHER.value}.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "dean",
    }

class SecretaryTable(UserTable) :
    __tablename__ = TableName.SECRETARY.value

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),ForeignKey(f"{TableName.USER.value}.entity_id"), primary_key=True)
    name = Column(String)

    __mapper_args__ = {
        "polymorphic_identity": "secretary",
    }


class AdministratorTable(UserTable) :
    __tablename__ = TableName.ADMINISTRATOR.value
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),ForeignKey(f"{TableName.USER.value}.entity_id"), primary_key=True)
    name = Column(String)

    __mapper_args__ = {
        "polymorphic_identity": "administrator",
    }


class StudentTable(UserTable) :
    __tablename__ = TableName.STUDENT.value

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),ForeignKey(f"{TableName.USER.value}.entity_id"), primary_key=True)
    name = Column(String)
    age = Column(Integer)
    extra_activities = Column(Boolean, nullable=True)
    average_note = Column(Double)
    course_id : Mapped[uuid.UUID] = mapped_column(ForeignKey(f"{TableName.COURSE.value}.entity_id"))
    """
    teacher: Mapped["Teacher"] = relationship(
        secondary=f"{TableName.TEACHER.value}", back_populates="students", viewonly=True
    )
    subject_notes: Mapped[List["Subject"]] = relationship(
        secondary=f"{TableName.SUBJECT.value}", back_populates="student_notes", viewonly=True
    )
    subject_absences: Mapped[List["Subject"]] = relationship(
        secondary=f"{TableName.ABSENCE.value}", back_populates="student_absences"
    )
    course: Mapped["Course"] = relationship(
        secondary=f"{TableName.COURSE.value}", back_populates="students"
    )
    """
    course: Mapped['CourseTable'] = relationship(back_populates="students")
    student_note_association: Mapped[List["StudentNoteTable"]] = relationship('StudentNoteTable', back_populates="student")
    student_absence_association: Mapped[List["AbsenceTable"]] = relationship(back_populates="student")
    teacher_note_association: Mapped[List["TeacherNoteTable"]] = relationship(back_populates="student")

    __mapper_args__ = {
        "polymorphic_identity": "student",
    }


class SubjectTable(BaseTable) :
    __tablename__ = TableName.SUBJECT.value

    name = Column(String)
    hourly_load  = Column(Integer)
    study_program = Column(Integer)

    classroom_id : Mapped[int] = mapped_column(ForeignKey(f"{TableName.CLASSROOM.value}.entity_id"))
    course_id : Mapped[uuid.UUID] = mapped_column(ForeignKey(f"{TableName.COURSE.value}.entity_id"))

    """
    teacher: Mapped["Teacher"] = relationship(
        secondary=f"{TableName.TEACHER.value}", back_populates="subjects", viewonly=True
    )
    student_notes: Mapped[List["Student"]] = relationship(
        secondary=f"{TableName.STUDENT.value}", back_populates="subjects", viewonly=True
    )
    student_absences: Mapped[List["Student"]] = relationship(
        secondary=f"{TableName.STUDENT.value}", back_populates="subject_absences", viewonly=True
    )
    course: Mapped["Course"] = relationship(
        secondary=f"{TableName.COURSE.value}", back_populates="subjects"
    )
    """
    
    classroom: Mapped["ClassroomTable"] = relationship(back_populates="subjects", cascade="all, delete")
    course: Mapped['CourseTable'] = relationship(back_populates="subjects", cascade="all, delete")

    student_teacher_association: Mapped[List["StudentNoteTable"]] = relationship(back_populates="subject", cascade="all, delete")
    student_absence_association: Mapped[List["AbsenceTable"]] = relationship(back_populates="subject", cascade="all, delete")
    teacher_note_association: Mapped[List["TeacherNoteTable"]] = relationship(back_populates="subject", cascade="all, delete")
    teacher_subject_association = relationship("TeacherTable", secondary=teacher_subject_table, back_populates="teacher_subject_association", cascade="all, delete")
    
class ClassroomTable(BaseTable) : 
    __tablename__ = TableName.CLASSROOM.value

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
    student_absence_association: Mapped[List["AbsenceTable"]] = relationship(back_populates="course")
    teacher_note_association: Mapped[List["TeacherNoteTable"]] = relationship(back_populates="course")



class MeanTable(BaseTable) :
    __tablename__ = TableName.MEAN.value
 
    name = Column(String) 
    state: Mapped[MeanState] = mapped_column(String)
    location = Column(String)
    classroom_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),ForeignKey(f"{TableName.CLASSROOM.value}.entity_id"))
    to_be_replaced = Column(Boolean, default=False)
    type: Mapped[MeanType] = mapped_column(String)

    mean_mainteniance_association: Mapped[List["MeanMaintenianceTable"]] = relationship(back_populates="mean")

    classroom: Mapped["ClassroomTable"] = relationship(back_populates="means")

    teachers = relationship(
        "TeacherTable",
        secondary=teacher_request_mean_table,
        back_populates="mean_request",
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
    student_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.STUDENT.value}.id"), primary_key=True)
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
    course_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.COURSE.value}.entity_id"))
    
    absences = Column(Integer)

    student: Mapped["StudentTable"] = relationship(back_populates="student_absence_association")
    subject: Mapped["SubjectTable"] = relationship(back_populates="student_absence_association")
    course: Mapped["CourseTable"] = relationship(back_populates="student_absence_association")



#Tablas de relación
class MeanMaintenianceTable(BaseTable) :
    __tablename__ = TableName.MEAN_MAINTENANCE_TABLE.value


    mean_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.MEAN.value}.entity_id"), primary_key= True)
    date_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.MY_DATE.value}.entity_id"), primary_key= True)
                                        
    cost = Column(Double)

    mean: Mapped["MeanTable"] = relationship(back_populates="mean_mainteniance_association")
    date = Column(DateTime, nullable=False)


class SanctionTable(BaseTable):
    __tablename__ = TableName.SANCTION.value

    teacher_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.TEACHER.value}.id"), nullable=False)
    teacher: Mapped["TeacherTable"] = relationship(back_populates="sanctions")
    amount: Mapped[Double] = mapped_column(Double, nullable=False)
    date = Column(DateTime, nullable=False)




    

         



    




