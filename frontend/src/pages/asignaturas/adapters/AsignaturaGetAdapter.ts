import { AsignaturaGetDB } from "../models/AsignaturaGetDB.ts";
import {ICursoGetLocal} from "../../cursos/models/ICursoGetLocal.ts";

export class AsignaturaGetAdapter {
    static Properties = ['ID' , 'Nombre', 'Carga Horaria', 'P de Estudio ' ,' Aula', 'Curso']
    id: string;
    name: string;
    hourly_load: number;
    study_program: number;
    classroom_id: string;
    course: ICursoGetLocal

    constructor(asignaturaGetDB: AsignaturaGetDB, curso: ICursoGetLocal) {
        this.id = asignaturaGetDB.id;
        this.name = asignaturaGetDB.name;
        this.hourly_load = asignaturaGetDB.hourly_load;
        this.study_program = asignaturaGetDB.study_program;
        this.classroom_id = asignaturaGetDB.classroom_id;
        this.course = curso;
    }
}