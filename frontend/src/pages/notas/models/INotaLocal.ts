
import {DBObject} from "../../../types.ts";
import {IEstudianteDB} from "../../estudiantes/models/IEstudianteDB.ts";
import {AsignaturaGetDB} from "../../asignaturas/models/AsignaturaGetDB.ts";
import {ProfesorDB} from "../../profesores/models/ProfesorGetDB.ts";
import {IUsuarioDB} from "../../usuarios/models/IUsuarioDB.ts";

export interface INotaLocal extends DBObject{
    id: string
    student: IEstudianteDB;
    subject: AsignaturaGetDB;
    teacher: ProfesorDB;
    last_modified_by: IUsuarioDB
    note_value: number
}