from backend.domain.schemas.teacher import TeacherModel
from backend.domain.models.tables import TeacherTable
from backend.application.serializers.subject import SubjectMapper
from pydantic import BaseModel
from datetime import datetime
from backend.domain.schemas.subject import SubjectModel
import uuid

"""
This module defines a mapper for converting teacher data into various API representations.

Classes:
    TeacherBetterThanEight: A Pydantic model representing teachers with an average valoration better than eight.
    TeacherTechnologicalClassroom: A Pydantic model representing teachers associated with technological classrooms.
    TeacherSanctions: A Pydantic model representing teachers with sanctions.
    TeacherMapper: A utility class for mapping TeacherTable objects to TeacherModel objects and handling various teacher-related data.

Class Details:

1. TeacherBetterThanEight:
    - Represents teachers with an average valoration better than eight.
    - Attributes:
        - name: The name of the teacher.
        - average_valoration: The average valoration of the teacher.
        - subjects: A list of subjects taught by the teacher.

2. TeacherTechnologicalClassroom:
    - Represents teachers associated with technological classrooms.
    - Attributes:
        - id: The unique identifier of the teacher.
        - name: The name of the teacher.
        - specialty: The specialty of the teacher.
        - mean: The mean associated with the teacher.
        - state: The state of the mean.

3. TeacherSanctions:
    - Represents teachers with sanctions.
    - Attributes:
        - name: The name of the teacher.
        - valorations: A list of valorations associated with the teacher.
        - date: The date of the sanction.
        - means: A boolean indicating if the teacher is associated with means.

4. TeacherMapper:
    - This class provides methods to convert TeacherTable objects and related data into various API models used in the application layer.
    
    Methods:
        - to_api(teacher: TeacherTable, subjects: list[str], valoration: float = None) -> TeacherModel: 
            Converts the given TeacherTable object into a TeacherModel object, mapping fields such as ID, name, lastname, email, specialty, contract type, experience, username, list of subjects, valoration, salary, and alert.
        - to_subject_list(subjects): 
            Converts a list of subject objects into a list of subject names.
        - to_teachers_with_average(data): 
            Converts raw data into a list of TeacherBetterThanEight objects, representing teachers with an average valoration better than eight.
        - to_teachers_technological_classroom(data): 
            Converts raw data into a list of TeacherTechnologicalClassroom objects, representing teachers associated with technological classrooms.
        - to_teachers_sanctions(data, mean_data): 
            Converts raw data into a list of TeacherSanctions objects, representing teachers with sanctions.
        - to_teachers_by_students(data): 
            Converts raw data into a list of TeacherModel objects, representing teachers associated with specific students.

Dependencies:
    - Pydantic for data validation and serialization.
    - TeacherModel for API data representation.
    - TeacherTable for database representation.
    - UUID and datetime for handling unique identifiers and date-time operations.
"""
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

class TeacherSubjectToEvaluate(BaseModel) :
    subjects_to_evaluate : list[SubjectModel]

class TeacherByStudent(BaseModel) :
    teacher : TeacherModel
    subject_to_evaluate : list[SubjectModel]

class TeacherMapper :

    def to_api(self, teacher: TeacherTable) -> TeacherModel :
        return TeacherModel(
            id = teacher.entity_id,
            name=teacher.name,
            lastname=teacher.lastname,
            email=teacher.email,
            specialty=teacher.specialty,
            contract_type=teacher.contract_type,
            experience=teacher.experience,
            username=teacher.username,
            subjects=self.to_subject_list(teacher.teacher_subject_association),
            valoration= teacher.average_valoration,
            salary=teacher.salary,
            alert=teacher.less_than_three_valoration 
        )
    
    def to_api_note(self, teacher:TeacherTable) :
        return TeacherModel(
            id = teacher.entity_id,
            name=teacher.name,
            lastname=teacher.lastname,
            email=teacher.email,
            specialty=teacher.specialty,
            contract_type=teacher.contract_type,
            experience=teacher.experience,
            username=teacher.username,
            subjects=self.to_subject_list(teacher.teacher_subject_association),
            valoration= teacher.average_valoration,
            salary=teacher.salary,
            alert=teacher.less_than_three_valoration 
        )

    
    def to_subject_list(self, subjects) :
        subjects_list = []
        subject_mapper = SubjectMapper()
        for subject in subjects :
            subjects_list.append(subject_mapper.to_api(subject))

        return subjects_list
            
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
        
        teacher_ids = []
        
        for teacher_id in mean_data :
            teacher_ids.append(teacher_id[0].id)
        
        for teacher in data :
            if teacher[0] in ids :
                serialized_values[len(serialized_values)-1].valorations.append(teacher[3])
            else :
                ids.append(teacher[0])
                
                new_teacher = TeacherSanctions(
                    name= teacher[1],
                    valorations= [teacher[3]] if teacher[3] else [],
                    date= teacher[2],
                    means= True if teacher[0] in teacher_ids else False
                )
                serialized_values.append(new_teacher)
            

        return serialized_values
    
    def to_teachers_by_students(self, big_data) :
        serialized_values = []
        teacher_ids = []
        subject_mapper = SubjectMapper()
        data = big_data[0]
        teacher_subject_to_evaluate = big_data[1]

        subjects_to_evaluate = self.subjects_to_evaluate(teacher_subject_to_evaluate)
        index = 0

        for teacher in data :
            if teacher[0].id in teacher_ids :
                serialized_values[len(serialized_values)-1].teacher.subjects.append(subject_mapper.to_api(teacher[1]))
            else :
                teacher_ids.append(teacher[0].id)
                new_teacher = TeacherModel(
                    id = teacher[0].id,
                    name= teacher[0].name,
                    lastname= teacher[0].lastname,
                    email= teacher[0].email,
                    specialty= teacher[0].specialty,
                    contract_type= teacher[0].contract_type,
                    experience= teacher[0].experience,
                    username= teacher[0].username,
                    subjects=[
                        subject_mapper.to_api(teacher[1])
                    ],
                    valoration= teacher[0].average_valoration,
                    salary=teacher[0].salary,
                    alert=teacher[0].less_than_three_valoration
                )
                
                new_teacher_with_subjects = TeacherByStudent(
                    teacher = new_teacher,
                    subject_to_evaluate = subjects_to_evaluate[index].subjects_to_evaluate
                )

                serialized_values.append(new_teacher_with_subjects)

        return serialized_values
    

    def subjects_to_evaluate(self, data) :
        serialized_values = []
        student = data[0][1]
        subjects = student.course.subjects

        for i, teacher_val in enumerate(data) :
            note = teacher_val[0]
            student = teacher_val[1]
            
            if note.subject in subjects :
                subjects.remove(note.subject)
            
            if i == len(data) - 1 : 
                new_teacher = TeacherSubjectToEvaluate(
                        subjects_to_evaluate = self.to_subject_list(subjects)
                    )
                
                serialized_values.append(new_teacher)
                subjects = student.course.subjects
              
            elif teacher_val.teacher_id != data[i+1][0].teacher_id :
                    new_teacher = TeacherSubjectToEvaluate(
                        subjects_to_evaluate = self.to_subject_list(subjects)
                    )

                    serialized_values.append(new_teacher)
                    subjects = student.course.subjects

        return serialized_values
    

        
        
        


    