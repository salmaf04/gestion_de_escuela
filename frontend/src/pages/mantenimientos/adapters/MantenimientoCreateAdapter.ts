import {MantenimientoCreateDto} from "../models/MantenimientoCreateDto.ts";

export class MantenimientoCreateAdapter {
    static Properties = ['Nombre', 'Apellidos', 'Especialidad', 'Contrato', 'Experiencia', 'Correo', 'Usuario', 'Mantenimientos']
    name: string
    hourly_load: number
    study_program: number
    classroom_id: string

    constructor(mantenimientoCreateDB: MantenimientoCreateDto) {
        this.name = mantenimientoCreateDB.name;
        this.hourly_load = mantenimientoCreateDB.hourly_load;
        this.classroom_id = mantenimientoCreateDB.classroom_id;
        this.study_program = mantenimientoCreateDB.study_program
    }
}