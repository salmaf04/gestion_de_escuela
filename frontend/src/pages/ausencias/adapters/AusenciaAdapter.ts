import {IAusenciaDB} from "../models/IAusenciaDB.ts";
import {IAusenciaLocal} from "../models/IAusenciaLocal.ts";
import {EstudianteGetAdapter} from "../../estudiantes/adapters/EstudianteGetAdapter.ts";
import {AsignaturaGetAdapter} from "../../asignaturas/adapters/AsignaturaGetAdapter.ts";

export class AusenciaAdapter implements IAusenciaLocal{
    static Properties = ['ID', 'Estudiante', 'Asignatura', 'Fecha']
    id: string
    student: EstudianteGetAdapter;
    subject: AsignaturaGetAdapter;
    date: string;

    constructor(nota: IAusenciaDB, student: EstudianteGetAdapter, subject: AsignaturaGetAdapter){
        this.id = nota.id
        this.date = nota.date
        this.student = student
        this.subject = subject
    }
}