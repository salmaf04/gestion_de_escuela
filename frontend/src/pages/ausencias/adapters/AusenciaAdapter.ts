import {IAusenciaDB} from "../models/IAusenciaDB.ts";
import {IAusenciaLocal} from "../models/IAusenciaLocal.ts";
import {IEstudianteDB} from "../../estudiantes/models/IEstudianteDB.ts";
import {AsignaturaGetDB} from "../../asignaturas/models/AsignaturaGetDB.ts";

export class AusenciaAdapter implements IAusenciaLocal{
    static Properties = ['ID', 'Estudiante', 'Asignatura', 'Cantidad']
    id: string
    student: IEstudianteDB
    subject: AsignaturaGetDB
    absences_total: number

    constructor(nota: IAusenciaDB){
        this.id = nota.id
        this.absences_total = nota.absences_total
        this.student = nota.student
        this.subject = nota.subject
    }
}