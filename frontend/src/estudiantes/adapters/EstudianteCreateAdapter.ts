import {EstudianteCreateDto} from "../models/EstudianteCreateDto.ts";

export class EstudianteCreateAdapter {
    static Properties = ['Nombre', 'Apellidos', 'Especialidad', 'Contrato', 'Experiencia', 'Correo', 'Usuario', 'Estudiantes']
    name: string
    hourly_load: number
    study_program: number
    classroom_id: string

    constructor(estudianteCreateDB: EstudianteCreateDto) {
        this.name = estudianteCreateDB.name;
        this.hourly_load = estudianteCreateDB.hourly_load;
        this.classroom_id = estudianteCreateDB.classroom_id;
        this.study_program = estudianteCreateDB.study_program
    }
}