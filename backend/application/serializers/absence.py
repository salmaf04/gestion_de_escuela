from backend.domain.schemas.absence import AbsenceModel
from backend.domain.schemas.student import StudentModel
from backend.domain.schemas.subject import SubjectModel
from backend.domain.models.tables import AbsenceTable
from backend.application.serializers.student import StudentMapper
from backend.application.serializers.subject import SubjectMapper
from pydantic import BaseModel
import uuid

class SubjectBySecretary(BaseModel) :
    student : StudentModel
    subject : SubjectModel
    absences_total : int

class SubjectByStudent(BaseModel) :
    subject : SubjectModel
    absences_total : int

class SubjectByStudentByTeacher(BaseModel) :
    student : StudentModel
    subject : SubjectModel
    absences_total : int
    
class AbsenceMapper :

    def to_api(self, absence: AbsenceTable) -> AbsenceModel :
        return AbsenceModel(
            id = absence.entity_id,
            student_id = absence.student_id,
            subject_id = absence.subject_id,
            date = absence.date.strftime("%d-%m-%Y")
        )
    
    def to_absence_by_secretary(self, data) :
        serialized_values = []
        subject_mapper = SubjectMapper()
        student_mapper = StudentMapper()

        for absence in data :
            serialized_values.append(
                SubjectByStudentByTeacher(
                    student=student_mapper.to_api(absence[3]),
                    subject=subject_mapper.to_api(absence[2]),
                    absences_total=absence[1]
                ) 
            )

        return serialized_values
    
    def to_abscence_by_student(self, data) :
        serialized_values = []
        subject_mapper = SubjectMapper()

        for absence in data :
            serialized_values.append(
                SubjectByStudent(
                    subject=subject_mapper.to_api(absence[2]),
                    absences_total=absence[1]
                ) 
            )
        
        return serialized_values
    
    def to_absence_by_student_by_teacher(self, data) :
        serialized_values = []
        subject_mapper = SubjectMapper()
        student_mapper = StudentMapper()

        for absence in data :
            serialized_values.append(
                SubjectByStudentByTeacher(
                    student=student_mapper.to_api(absence[3]),
                    subject=subject_mapper.to_api(absence[2]),
                    absences_total=absence[1]
                ) 
            )

        return serialized_values

    
    