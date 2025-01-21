import { AsignaturaGetDB } from "../models/AsignaturaGetDB.ts";

export class AsignaturaGetAdapter {
    static Properties = ['Nombre', 'Carga Horaria', 'P de Estudio ']
    id: string;
    name: string;
    hourly_load: number;
    study_program: number;
    classroom_id: string;

    constructor(asignaturaGetDB: AsignaturaGetDB) {
        this.id = asignaturaGetDB.id;
        this.name = asignaturaGetDB.name;
        this.hourly_load = asignaturaGetDB.hourly_load;
        this.study_program = asignaturaGetDB.study_program;
        this.classroom_id = asignaturaGetDB.classroom_id;
    }
}