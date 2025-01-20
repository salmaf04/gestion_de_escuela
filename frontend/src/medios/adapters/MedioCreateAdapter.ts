import {MedioCreateDto} from "../models/MedioCreateDto.ts";

export class MedioCreateAdapter {
    static Properties = ['Nombre', 'Apellidos', 'Especialidad', 'Contrato', 'Experiencia', 'Correo', 'Usuario', 'Medios']
    name: string
    hourly_load: number
    study_program: number
    classroom_id: string

    constructor(medioCreateDB: MedioCreateDto) {
        this.name = medioCreateDB.name;
        this.hourly_load = medioCreateDB.hourly_load;
        this.classroom_id = medioCreateDB.classroom_id;
        this.study_program = medioCreateDB.study_program
    }
}