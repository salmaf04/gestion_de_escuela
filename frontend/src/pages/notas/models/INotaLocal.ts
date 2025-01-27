import {ProfesorGetAdapter} from "../../profesores/adapters/ProfesorGetAdapter.ts";
import {EstudianteGetAdapter} from "../../estudiantes/adapters/EstudianteGetAdapter.ts";
import {AsignaturaGetAdapter} from "../../asignaturas/adapters/AsignaturaGetAdapter.ts";
import {DBObject} from "../../../types.ts";

export interface INotaLocal extends DBObject{
    id: string,
    teacher: ProfesorGetAdapter,
    student: EstudianteGetAdapter,
    subject: AsignaturaGetAdapter,
    note_value: number
}