from backend.domain.schemas.teacher import TeacherModel
from backend.domain.models.tables import TeacherTable
from pydantic import BaseModel


class TeacherBetterThanEight(BaseModel) :
    name : str
    average_valoration : float
    subjects : list[str]


class TeacherTechnologicalClassroom(BaseModel) :
    name : str
    classroom_id : list[str]
    mean : list[str]
class TeacherMapper :

    def to_api(self, teacher: TeacherTable , subjects: list[str] , valoration: float = None) -> TeacherModel :
        return TeacherModel(
            id = teacher.entity_id,
            name=teacher.name,
            fullname=teacher.fullname,
            email=teacher.email,
            specialty=teacher.specialty,
            contract_type=teacher.contract_type,
            experience=teacher.experience,
            username=teacher.username,
            list_of_subjects=subjects,
            valoration= teacher.average_valoration
        )
    
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
        serialized_values = {}

        for teachers in data :
            if teachers[0].name  in serialized_values :
                serialized_values[teachers[0].name].append(teachers[2].entity_id)
            else :
                serialized_values[teachers[0].name] = [teachers[2].entity_id]

        return serialized_values

    