import {EstudianteGetAdapter} from "../../estudiantes/adapters/EstudianteGetAdapter.ts";
import {AsignaturaGetAdapter} from "../../asignaturas/adapters/AsignaturaGetAdapter.ts";
import {DBObject} from "../../../types.ts";

export interface IAusenciaLocal extends DBObject{
    id: string,
    student: EstudianteGetAdapter,
    subject: AsignaturaGetAdapter,
    absences_total: number
}