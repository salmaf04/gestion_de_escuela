import { AsignaturaCreateDB } from "../models/AsignaturaCreateDB.ts";

export class AsignaturaCreateAdapter {
    name: string;
    hourly_load: number;
    study_program: number;
    classroom_id: string;
    course_id: string

    constructor(asignaturaCreateDB: AsignaturaCreateDB) {
        this.name = asignaturaCreateDB.name;
        this.hourly_load = asignaturaCreateDB.hourly_load;
        this.study_program = asignaturaCreateDB.study_program;
        this.classroom_id = asignaturaCreateDB.classroom_id;
        this.course_id = asignaturaCreateDB.course_id;
    }
}