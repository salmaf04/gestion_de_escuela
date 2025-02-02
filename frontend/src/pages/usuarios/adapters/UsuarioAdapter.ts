import {IUsuarioDB} from "../models/IUsuarioDB.ts";
import {IUsuarioLocal} from "../models/IUsuarioLocal.ts";
import {EstudianteGetAdapter} from "../../estudiantes/adapters/EstudianteGetAdapter.ts";
import {AsignaturaGetAdapter} from "../../asignaturas/adapters/AsignaturaGetAdapter.ts";
import {ProfesorGetAdapter} from "../../profesores/adapters/ProfesorGetAdapter.ts";

export class UsuarioAdapter implements IUsuarioLocal{
    static Properties = ['ID', 'Profesor', 'Estudiante', 'Asignatura', 'Nota']
    id: string
    note_value: number;
    student: EstudianteGetAdapter;
    subject: AsignaturaGetAdapter;
    teacher: ProfesorGetAdapter;
    dbObject: IUsuarioDB

    constructor(nota: IUsuarioDB, student: EstudianteGetAdapter, subject: AsignaturaGetAdapter, teacher: ProfesorGetAdapter){
        this.id = nota.id
        this.dbObject = nota
        this.note_value = nota.note_value
        this.student = student
        this.subject = subject
        this.teacher = teacher
    }
}