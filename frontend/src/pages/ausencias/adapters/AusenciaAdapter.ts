import {IAusenciaDB} from "../models/IAusenciaDB.ts";
import {IAusenciaLocal} from "../models/IAusenciaLocal.ts";
import {IEstudianteDB} from "../../estudiantes/models/IEstudianteDB.ts";
import {AsignaturaGetDB} from "../../asignaturas/models/AsignaturaGetDB.ts";
import {IDateAusencia} from "../models/IDateAusencia.ts";

export class AusenciaAdapter implements IAusenciaLocal{
    static Properties = ['ID', 'Estudiante', 'Asignatura', 'Cantidad']
    id: string
    student: IEstudianteDB
    subject: AsignaturaGetDB
    dates: IDateAusencia[]
    absences_total: number

    constructor(ausencia: IAusenciaDB, index: string){
        this.id = index
        this.absences_total = ausencia.absences_total
        this.student = ausencia.student
        this.subject = ausencia.subject
        this.dates = ausencia.dates
    }
}