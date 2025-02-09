import {IEstudianteDB} from "../../estudiantes/models/IEstudianteDB.ts";
import {AsignaturaGetDB} from "../../asignaturas/models/AsignaturaGetDB.ts";
import {IDateAusencia} from "./IDateAusencia.ts";

export interface IAusenciaDB {
    student: IEstudianteDB
    subject: AsignaturaGetDB
    dates: IDateAusencia[]
    absences_total: number
}