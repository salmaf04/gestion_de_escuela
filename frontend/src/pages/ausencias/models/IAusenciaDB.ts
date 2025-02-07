import {IEstudianteDB} from "../../estudiantes/models/IEstudianteDB.ts";
import {AsignaturaGetDB} from "../../asignaturas/models/AsignaturaGetDB.ts";

export interface IAusenciaDB {
    id: string
    student: IEstudianteDB,
    subject: AsignaturaGetDB,
    absences_total: number,
}