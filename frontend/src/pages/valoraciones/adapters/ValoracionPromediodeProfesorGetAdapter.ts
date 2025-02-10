import { ValoracionPorAsignaturaDeProfesorGetDB } from "../models/models.ts";

export class ValoracionPorAsignaturadeProfesorGetAdapter {
    id: string;
    teacherName: string;
    teacherLastname: string;
    subjectName: string;
    courseYear: number;
    valoration : number

    constructor(data: ValoracionPorAsignaturaDeProfesorGetDB) {
        this.id = data.id;
        this.teacherName = data.teacher.name;
        this.teacherLastname = data.teacher.lastname;
        this.subjectName = data.subject.name;
        this.courseYear = data.course.year;
        this.valoration = data.grade
    }
    [key: string]: any;
}