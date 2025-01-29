import {INotaDB} from "../models/INotaDB.ts";
import {INotaLocal} from "../models/INotaLocal.ts";
import {EstudianteGetAdapter} from "../../estudiantes/adapters/EstudianteGetAdapter.ts";
import {AsignaturaGetAdapter} from "../../asignaturas/adapters/AsignaturaGetAdapter.ts";
import {ProfesorGetAdapter} from "../../profesores/adapters/ProfesorGetAdapter.ts";

export class NotaAdapter implements INotaLocal{
    static Properties = ['ID', 'Profesor', 'Estudiante', 'Asignatura', 'Nota']
    id: string
    note_value: number;
    student: EstudianteGetAdapter;
    subject: AsignaturaGetAdapter;
    teacher: ProfesorGetAdapter;
    dbObject: INotaDB

    constructor(nota: INotaDB, student: EstudianteGetAdapter, subject: AsignaturaGetAdapter, teacher: ProfesorGetAdapter){
        this.id = nota.id
        this.dbObject = nota
        this.note_value = nota.note_value
        this.student = student
        this.subject = subject
        this.teacher = teacher
    }
}