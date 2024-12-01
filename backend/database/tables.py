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
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

import uuid

class TableName(str, Enum):
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


class UserTable(BaseTable) :
    __tablename__ = "user"
    
    username = Column(String, unique=True)
    email = Column(String, unique =True)
    hash_password = Column(String)


class TeacherTable(BaseTable):
    __tablename__ = TableName.TEACHER.value
    
    name = Column(String)
    fullname = Column(String)
    specialty = Column(String)
    contract_type = Column(String)
    experience = Column(Integer)
    type = Column(String)
    """
    students: Mapped[List["Student"]] = relationship(
        secondary=f"{TableName.STUDENT.value}", back_populates="teacher", viewonly=True
    )
    subjects: Mapped[List["Subject"]] = relationship(
        secondary=f"{TableName.SUBJECT.value}", back_populates="teacher", viewonly=True
    )
    """

    student_note_association: Mapped[List["StudentNoteTable"]] = relationship(back_populates="teacher")
    teacher_note_association: Mapped[List["TeacherNoteTable"]] = relationship(back_populates="teacher")

      
class DeanTable(TeacherTable):
    __tablename__ = TableName.DEAN.value
    
    teacher_id = Column(Integer,primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "dean",
        "inherit_condition": id == teacher_id
    }
    

class SecretaryTable(BaseTable) :
    __tablename__ = TableName.SECRETARY.value

    name = Column(String)


class AdministratorTable(BaseTable) :
    __tablename__ = TableName.ADMINISTRATOR.value

    name = Column(String)


class StudentTable(BaseTable) :
    __tablename__ = TableName.STUDENT.value

    name = Column(String)
    age = Column(Integer)
    email = Column(String, unique=True)
    extra_activities = Column(Boolean, nullable=True)
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
    student_note_association: Mapped[List["StudentNoteTable"]] = relationship(back_populates="student")
    student_absence_association: Mapped[List["AbsenceTable"]] = relationship(back_populates="student")
    teacher_note_association: Mapped[List["TeacherNoteTable"]] = relationship(back_populates="student")


class SubjectTable(BaseTable) :
    __tablename__ = TableName.SUBJECT.value

    name = Column(String)
    hourly_load  = Column(Integer)
    study_program = Column(Integer)
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
    student_teacher_association: Mapped[List["StudentNoteTable"]] = relationship(back_populates="subject")
    student_absence_association: Mapped[List["AbsenceTable"]] = relationship(back_populates="subject")
    teacher_note_association: Mapped[List["TeacherNoteTable"]] = relationship(back_populates="subject")

    
class ClassroomTable(BaseTable) : 
    __tablename__ = TableName.CLASSROOM.value

    location = Column(String)
    capacity = Column(Integer)


class CourseTable(BaseTable) :
    __tablename__ = TableName.COURSE.value
    """
    students: Mapped[List["Student"]] = relationship(
        secondary=f"{TableName.STUDENT.value}", back_populates="course"
    )
    subjects: Mapped[List["Subject"]] = relationship(
        secondary=f"{TableName.SUBJECT.value}", back_populates="course"
    )
    """
    student_absence_association: Mapped[List["AbsenceTable"]] = relationship(back_populates="course")
    teacher_note_association: Mapped[List["TeacherNoteTable"]] = relationship(back_populates="course")

    course = Column(Integer , nullable=False , unique=True)


class MeanTable(BaseTable) :
    __tablename__ = TableName.MEAN.value
 
    name = Column(String) 
    state: Mapped[MeanState] = mapped_column(String)
    location = Column(String)
    type: Mapped[MeanType] = mapped_column(String)

    mean_mainteniance_association: Mapped[List["MeanMaintenianceTable"]] = relationship(back_populates="mean")

    __mapper_args__ = {
        "polymorphic_on": "type",
    }


class TechnologicalMeanTable(MeanTable) : 
    __tablename__ = TableName.TECHNOLOGICAL_MEAN.value  

    mean_id = Column(Integer, primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "technological mean",
        "inherit_condition": id == mean_id
    }


class TeachingMaterialTable(MeanTable) : 
    __tablename__ = TableName.TEACHING_MATERIAL.value   

    mean_id = Column(Integer,primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "teaching_material",
        "inherit_condition": id == mean_id
    }


class OthersTable(MeanTable) : 
    __tablename__ = TableName.OTHERS.value

    mean_id = Column(Integer, primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "other",
        "inherit_condition": id == mean_id
    }


class MyDateTable(BaseTable):
    __tablename__ = TableName.MY_DATE.value

    date = Column(DateTime, unique= True)

    mean_mainteniance_association: Mapped[List["MeanMaintenianceTable"]] = relationship(back_populates="date")
    

class StudentNoteTable(BaseTable) :
    __tablename__ = TableName.STUDENT_NOTE.value

    teacher_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.TEACHER.value}.entity_id"))
    student_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.STUDENT.value}.entity_id"), primary_key=True)
    subject_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.SUBJECT.value}.entity_id"), primary_key=True)
    
    note_value = Column(Integer)
    
    teacher: Mapped["TeacherTable"] = relationship(back_populates="student_note_association")
    student: Mapped["StudentTable"] = relationship(back_populates="student_note_association")
    subject: Mapped["SubjectTable"] = relationship(back_populates="student_teacher_association")


class TeacherNoteTable(BaseTable) :
    __tablename__ = TableName.TEACHER_NOTE.value

    teacher_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.TEACHER.value}.entity_id"), primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.STUDENT.value}.entity_id"), primary_key=True)
    subject_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.SUBJECT.value}.entity_id"), primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.COURSE.value}.entity_id"))
    
    grade = Column(Integer)

    teacher: Mapped["TeacherTable"] = relationship(back_populates="teacher_note_association")
    student: Mapped["StudentTable"] = relationship(back_populates="teacher_note_association")
    subject: Mapped["SubjectTable"] = relationship(back_populates="teacher_note_association")
    course: Mapped["CourseTable"] = relationship(back_populates="teacher_note_association")
        
    

class AbsenceTable(BaseTable) :
    __tablename__ = TableName.ABSENCE.value

    student_id: Mapped[int] = mapped_column(ForeignKey(f"{TableName.STUDENT.value}.entity_id"), primary_key=True)
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
    date: Mapped["MyDateTable"] = relationship(back_populates="mean_mainteniance_association")



    

         



    




