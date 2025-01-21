import {AsignaturaCreateDto} from "../models/AsignaturaCreateDB.ts";

export class AsignaturaCreateAdapter {
    static Properties = ['Nombre', 'Apellidos', 'Especialidad', 'Contrato', 'Experiencia', 'Correo', 'Usuario', 'Asignaturas']
    name: string
    hourly_load: number
    study_program: number
    classroom_id: string

    constructor(asignaturaCreateDB: AsignaturaCreateDto) {
        this.name = asignaturaCreateDB.name;
        this.hourly_load = asignaturaCreateDB.hourly_load;
        this.classroom_id = asignaturaCreateDB.classroom_id;
        this.study_program = asignaturaCreateDB.study_program
    }
}