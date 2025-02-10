import {ProfesorDB} from "../../profesores/models/ProfesorGetDB.ts";
import {IEstudianteDB} from "../../estudiantes/models/IEstudianteDB.ts";
import {AsignaturaGetDB} from "../../asignaturas/models/AsignaturaGetDB.ts";
import {IUsuarioDB} from "../../usuarios/models/IUsuarioDB.ts";

export interface INotaDB {
    id: string
    teacher: ProfesorDB,
    student: IEstudianteDB,
    subject: AsignaturaGetDB,
    last_modified_by: IUsuarioDB
    note_value: number,
}