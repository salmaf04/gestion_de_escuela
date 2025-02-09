import {ICursoGetDB} from "../../cursos/models/ICursoGetDB.ts";
import {AulaGetDB} from "../../aulas/models/AulaGetDB.ts";

export type AsignaturaGetDB = {

    id : string;
    name: string;
    hourly_load: number;
    study_program: number;
    classroom: AulaGetDB;
    course: ICursoGetDB
}

export type AsignaturaGetResponse = AsignaturaGetDB[]