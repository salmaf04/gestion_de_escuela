export enum EndpointEnum {
    PROFESORES = "teacher",
    ESTUDIANTES = "student",
    AULAS = 'classroom',
    MEDIOS = 'mean',
    ASIGNATURAS = 'subject',
    NOTAS = 'note',
    CURSOS = 'course',
    MANTENIMIENTOS = 'mean_maintenance',
    CLASSROOM_REQUEST = 'classroom_request',
    MEAN_REQUEST = 'mean_request',
    VALORATION = 'valoration',
    ESP_PROFESOR = 'teacher/?technology_classroom=true',
    FILTRO_DE_MANTENIMENTO = 'mean_maintenance/?mainteniance_by_classroom_filter=true',
    COSTO_PROMEDIO = 'mean_maintenance/?date_filter=true',
    VALORACION_PROMEDIO_PROFESOR = 'teacher/?better_than_eight=true ',
    VALORACION_PROMEDIO_ESTUDIANTE = 'student/?student_note_less_than_fifty=true',
    SALARIOS_PROFESORES = 'teacher/?sanctions=true'
}