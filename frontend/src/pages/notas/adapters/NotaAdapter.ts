import {INotaDB} from "../models/INotaDB.ts";
import {INotaLocal} from "../models/INotaLocal.ts";
import {IEstudianteDB} from "../../estudiantes/models/IEstudianteDB.ts";
import {AsignaturaGetDB} from "../../asignaturas/models/AsignaturaGetDB.ts";
import {ProfesorDB} from "../../profesores/models/ProfesorGetDB.ts";

export class NotaAdapter implements INotaLocal{
    static Properties = ['ID', 'Profesor', 'Estudiante', 'Asignatura', 'Nota']
    id: string
    note_value: number;
    student: IEstudianteDB;
    subject: AsignaturaGetDB;
    teacher: ProfesorDB;
    dbObject: INotaDB

    constructor(nota: INotaDB){
        this.id = nota.id
        this.dbObject = nota
        this.note_value = nota.note_value
        this.student = nota.student
        this.subject = nota.subject
        this.teacher = nota.teacher
    }
}