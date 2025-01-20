import {AulaCreateDto} from "../models/MedioCreateDto.ts";

export class AulaCreateAdapter {
    static Properties = ['Nombre', 'Apellidos', 'Especialidad', 'Contrato', 'Experiencia', 'Correo', 'Usuario', 'Aulas']
    name: string
    hourly_load: number
    study_program: number
    classroom_id: string

    constructor(aulaCreateDB: AulaCreateDto) {
        this.name = aulaCreateDB.name;
        this.hourly_load = aulaCreateDB.hourly_load;
        this.classroom_id = aulaCreateDB.classroom_id;
        this.study_program = aulaCreateDB.study_program
    }
}