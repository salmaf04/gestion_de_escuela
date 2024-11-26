from typing import List
from typing import Optional
from enum import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

class TableNames(str, Enum):
    PROFESOR = "profesor" 
    DECANO = "decano"
    ASIGNATURA = "asignatura"
    Estudiante = "estudiante"

class EstadoMedios(str, Enum):
    EXCELENTE = "excelente" 
    BIEN = "bien"
    REGULAR = "regular"
    MAL = "mal"    

class TipoMedios(str, Enum) :
    TECNOLÓGICOS = "tecnológicos"
    MATERIAL_DIDÁCTICO = "material didáctico"
    OTROS = "otros"


class BaseTable(DeclarativeBase):
    entity_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class User(DeclarativeBase) :
    __tablename__ = "user"

    username = Column(String, unique=True)
    email = Column(String, unique =True)
    hash_password = Column(String)


class Profesor(BaseTable):
    __tablename__ = "profesor"
    
    name = Column(String)
    fullname = Column(String)
    especialidad = Column(String)
    tipo_de_contrato = Column(String)
    experiencia = Column(Integer)


class Decano(BaseTable , Profesor):
    __tablename__ = "decano"
    
    __mapper_args__ = {
        "polymorphic_identity": "decano",
    }
    

class Secretaria(BaseTable) :
    __tablename__ = "secretaria"

    nombre = Column(String)


class Administrador(BaseTable) :
    __tablename__ = "administrador"

    nombre = Column(String)


class Estudiante(BaseTable) :
    __tablename__ = "estudiante"

    nombre = Column(String)
    edad = Column(Integer)
    actividades_extras = Column(Boolean, nullable=True)


class Asignatura(BaseTable) :
    __tablename__ = "asignatura"

    nombre = Column(String)
    carga_horaria  = Column(Integer)
    programa_de_estudios = Column(Integer)


class Aula(BaseTable) : 
    __tablename__ = "aula"

    ubicación = Column(String)
    capacidad = Column(Integer)


class Curso(BaseTable) :
    __tablename__ = "curso"

    curso = Column(Integer , nullable=False , unique=True)


class Medio(BaseTable) :
    __tablename__ = "medio"
 
    nombre = Column(String) 
    estado: Mapped[EstadoMedios] = mapped_column(String)
    ubicación = Column(String)
    tipo: Mapped[TipoMedios] = mapped_column(String)


class MedioTecnologico(Medio, BaseTable) : 
    __tablename__ = "medio tecnologico"   

    __mapper_args__ = {
        "polymorphic_identity": "medio tecnologico",
        "polymorphic_on": "tipo"
    }


class MaterialDidactico(Medio, BaseTable) : 
    __tablename__ = "material didactico"   

    __mapper_args__ = {
        "polymorphic_identity": "material didactico",
        "polymorphic_on": "tipo"
    }


class Otros(Medio, BaseTable) : 
    __tablename__ = "otros"   

    __mapper_args__ = {
        "polymorphic_identity": "otros",
        "polymorphic_on": "tipo"
    }
    
    



    




