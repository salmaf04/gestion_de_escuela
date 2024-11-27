from typing import List
from typing import Optional
from enum import Enum
from sqlalchemy import ForeignKey, Table
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import Boolean
from sqlalchemy import DateTime
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


class User(DeclarativeBase) :
    __tablename__ = "user"

    username = Column(String, unique=True)
    email = Column(String, unique =True)
    hash_password = Column(String)


class Teacher(BaseTable):
    __tablename__ = TableName.TEACHER.value
    
    name = Column(String)
    fullname = Column(String)
    specialty = Column(String)
    contract_type = Column(String)
    experience = Column(Integer)


class Dean(BaseTable , Teacher):
    __tablename__ = TableName.DEAN.value
    
    __mapper_args__ = {
        "polymorphic_identity": "dean",
    }
    

class Secretary(BaseTable) :
    __tablename__ = TableName.SECRETARY.value

    name = Column(String)


class Administrator(BaseTable) :
    __tablename__ = TableName.ADMINISTRATOR.value

    name = Column(String)


class Student(BaseTable) :
    __tablename__ = TableName.STUDENT.value

    name = Column(String)
    age = Column(Integer)
    extra_activities = Column(Boolean, nullable=True)


class Subject(BaseTable) :
    __tablename__ = TableName.SUBJECT.value

    name = Column(String)
    hourly_load  = Column(Integer)
    study_program = Column(Integer)


class Classroom(BaseTable) : 
    __tablename__ = TableName.CLASSROOM.value

    location = Column(String)
    capacity = Column(Integer)


class Course(BaseTable) :
    __tablename__ = TableName.COURSE.value

    course = Column(Integer , nullable=False , unique=True)


class Mean(BaseTable) :
    __tablename__ = TableName.MEAN.value
 
    name = Column(String) 
    state: Mapped[MeanState] = mapped_column(String)
    location = Column(String)
    type: Mapped[MeanType] = mapped_column(String)


class TechnologicalMean(Mean, BaseTable) : 
    __tablename__ = TableName.TECHNOLOGICAL_MEAN.value  

    __mapper_args__ = {
        "polymorphic_identity": "technological mean",
        "polymorphic_on": "type"
    }


class TeachingMaterial(Mean, BaseTable) : 
    __tablename__ = TableName.TEACHING_MATERIAL.value   

    __mapper_args__ = {
        "polymorphic_identity": "teaching material" ,
        "polymorphic_on": "type"
    }


class Others(Mean, BaseTable) : 
    __tablename__ = TableName.OTHERS.value

    __mapper_args__ = {
        "polymorphic_identity": "others",
        "polymorphic_on": "type"
    }
    
class MyDate (BaseTable):
    __tablename__ = TableName.MY_DATE.value

    date = Column(DateTime, unique= True)
    
class StudentNote (BaseTable) :
    __tablename__ = TableName.STUDENT_NOTE.value
    
#Tablas de relación
mean_maintenance_table = Table(
    TableName.MEAN_MAINTENANCE_TABLE.value,
    BaseTable.metadata,
    Column("mean_id", ForeignKey(f"{TableName.MEAN}.entity_id", use_alter=True), primary_key= True),
    Column("date_id", ForeignKey(f"{TableName.MY_DATE}.entity_id", use_alter=True), primary_key= True),
)
    
    



    




