import {IAusenciaDB} from "../models/IAusenciaDB.ts";
import {IAusenciaLocal} from "../models/IAusenciaLocal.ts";
import {EstudianteGetAdapter} from "../../estudiantes/adapters/EstudianteGetAdapter.ts";
import {AsignaturaGetAdapter} from "../../asignaturas/adapters/AsignaturaGetAdapter.ts";

export class AusenciaAdapter implements IAusenciaLocal{
    static Properties = ['ID', 'Estudiante', 'Asignatura', 'Ausencias']
    id: string
    student: EstudianteGetAdapter;
    subject: AsignaturaGetAdapter;
    absences_total: number;

    constructor(nota: IAusenciaDB, student: EstudianteGetAdapter, subject: AsignaturaGetAdapter){
        this.id = nota.id
        this.student = student
        this.subject = subject
        this.absences_total = nota.absences_total
    }
}