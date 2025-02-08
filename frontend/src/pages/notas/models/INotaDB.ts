import {ProfesorDB} from "../../profesores/models/ProfesorGetDB.ts";
import {IEstudianteDB} from "../../estudiantes/models/IEstudianteDB.ts";
import {AsignaturaGetDB} from "../../asignaturas/models/AsignaturaGetDB.ts";

export interface INotaDB {
    id: string
    teacher: ProfesorDB,
    student: IEstudianteDB,
    subject: AsignaturaGetDB,
    note_value: number,
}