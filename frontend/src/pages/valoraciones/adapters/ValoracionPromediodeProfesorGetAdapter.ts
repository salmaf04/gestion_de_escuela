import { ValoracionPorAsignaturaDeProfesorGetDB } from "../models/models.ts";

export class ValoracionPorAsignaturadeProfesorGetAdapter {

    teacherName: string;
    teacherLastname: string;
    subjectName: string;
    courseYear: number;
    valoration : number

    constructor(data: ValoracionPorAsignaturaDeProfesorGetDB) {
        this.teacherName = data.teacher.name;
        this.teacherLastname = data.teacher.lastname;
        this.subjectName = data.subject.name;
        this.courseYear = data.subject.course.year;
        this.valoration = data.average_valoration
    }
    [key: string]: any;
}