import {DBObject} from "../../../types.ts";
import {IEstudianteDB} from "../../estudiantes/models/IEstudianteDB.ts";
import {AsignaturaGetDB} from "../../asignaturas/models/AsignaturaGetDB.ts";
import {IDateAusencia} from "./IDateAusencia.ts";

export interface IAusenciaLocal extends DBObject{
    student: IEstudianteDB,
    subject: AsignaturaGetDB,
    dates: IDateAusencia[]
    absences_total: number
}