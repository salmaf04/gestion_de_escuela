import { AsignaturaGetDB } from "../models/AsignaturaGetDB.ts";
import {ICursoGetDB} from "../../cursos/models/ICursoGetDB.ts";
import {AulaGetDB} from "../../aulas/models/AulaGetDB.ts";

export class AsignaturaGetAdapter {
    static Properties = ['ID' , 'Nombre', 'Carga Horaria', 'Programa de Estudio ' ,' Aula', 'Curso']
    id: string;
    name: string;
    hourly_load: number;
    study_program: number;
    classroom: AulaGetDB;
    course: ICursoGetDB
    average_note: number

    constructor(asignaturaGetDB: AsignaturaGetDB) {
        this.id = asignaturaGetDB.id;
        this.name = asignaturaGetDB.name;
        this.hourly_load = asignaturaGetDB.hourly_load;
        this.study_program = asignaturaGetDB.study_program;
        this.classroom = asignaturaGetDB.classroom;
        this.course = asignaturaGetDB.course;
        this.average_note = asignaturaGetDB.average_note
    }
}