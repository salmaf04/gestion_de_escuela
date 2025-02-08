
import {DBObject} from "../../../types.ts";
import {IEstudianteDB} from "../../estudiantes/models/IEstudianteDB.ts";
import {AsignaturaGetDB} from "../../asignaturas/models/AsignaturaGetDB.ts";
import {ProfesorDB} from "../../profesores/models/ProfesorGetDB.ts";

export interface INotaLocal extends DBObject{
    id: string
    student: IEstudianteDB;
    subject: AsignaturaGetDB;
    teacher: ProfesorDB;
    note_value: number
}