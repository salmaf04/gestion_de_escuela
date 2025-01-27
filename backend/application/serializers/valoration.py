from backend.domain.schemas.valoration import ValorationModel, TeacherValoration, TeacherSubjectValoration
from backend.domain.models.tables import TeacherNoteTable


class ValorationMapper :

    def to_api(self, valoration: TeacherNoteTable) -> ValorationModel :
        return ValorationModel(
            id = valoration.entity_id,
            teacher_id = valoration.teacher_id,
            student_id = valoration.student_id,
            subject_id = valoration.subject_id,
            course_id = valoration.course_id,
            grade = valoration.grade
        )
    
    def to_valoration_by_subject(self, data) :
        started = False
        
        for average in data :
            if not started :
                started = True
                student = TeacherValoration(
                    id = average.teacher_id,
                    performance = [
                        TeacherSubjectValoration(
                            subject_id = average.subject_id,
                            average_subject_performance = average.valoration
                        )
                    ]
                )
            else :
                student.performance.append(
                    TeacherSubjectValoration(
                        subject_id = average.subject_id,
                        average_subject_performance = average.valoration
                    )
                )
                
        return student