from backend.domain.schemas.teacher import TeacherModel
from backend.domain.models.tables import TeacherTable
from pydantic import BaseModel
from datetime import datetime
import uuid
from fpdf import FPDF

class TeacherBetterThanEight(BaseModel) :
    name : str
    average_valoration : float
    subjects : list[str]


class TeacherTechnologicalClassroom(BaseModel) :
    name : str
    classroom_id : list[str]
    mean : list[str]


class TeacherSanctions(BaseModel) :
    name :str 
    valorations : list[int]
    date : datetime
    means : bool


class TeacherTechnologicalClassroom(BaseModel) :
    id : uuid.UUID
    name : str
    specialty : str
    mean : str
    state : str


class TeacherMapper :

    def to_api(self, teacher: TeacherTable , subjects: list[str] , valoration: float = None) -> TeacherModel :
        return TeacherModel(
            id = teacher.entity_id,
            name=teacher.name,
            lastname=teacher.lastname,
            email=teacher.email,
            specialty=teacher.specialty,
            contract_type=teacher.contract_type,
            experience=teacher.experience,
            username=teacher.username,
            list_of_subjects=subjects,
            valoration= teacher.average_valoration,
            salary=teacher.salary
        )
    

    def to_pdf(self, resultados) -> TeacherModel :
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Agregar los datos al PDF
        for resultado in resultados:
            line = f"ID: {resultado.id}, Nombre: {resultado.name}, Especialidades: {resultado.specialty}, Email: {resultado.email}, Salario: {resultado.salary}"
            pdf.cell(400, 20, txt=line, ln=True)

        # Guardar el PDF
        pdf.output("resultado.pdf")


    
    def to_subject_list(self, subjects) :
        names = []
        for subject in subjects :
            names.append(subject.name)
        return names
    
    def to_teachers_with_average(self, data) :
        serialized_values = []

        for teacher, subjects in zip(data[0], data[1]) :
            new_teacher = TeacherBetterThanEight(
                name= teacher.name,
                average_valoration= teacher.average_valoration,
                subjects= subjects
            )
            serialized_values.append(new_teacher)

        return list(serialized_values)
    

    def to_teachers_technological_classroom(self, data) :
        serialized_values = []

        for items in data :
            new_teacher = TeacherTechnologicalClassroom(
                id = items[0].id,
                name = items[0].name,
                specialty = items[0].specialty,
                mean = items[3],
                state = items[4]
            )
            serialized_values.append(new_teacher)

        return serialized_values
    
    
    def to_teachers_sanctions(self, data, mean_data) :
        serialized_values = []
        ids = []
        
        print(len(data))

        for teacher in data :
            if teacher[0] in ids :
                serialized_values[len(serialized_values)-1].valorations.append(teacher[3])
            else :
                ids.append(teacher[0])
                
                new_teacher = TeacherSanctions(
                    name= teacher[1],
                    valorations= [teacher[3]] if teacher[3] else [],
                    date= teacher[2],
                    means= True if teacher[0] in mean_data else False
                )
                serialized_values.append(new_teacher)
            

        return serialized_values
    

        
        
        


    