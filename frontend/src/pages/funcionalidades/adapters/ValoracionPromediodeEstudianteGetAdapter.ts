import { ValoracionPromediodeEstudianteGetDB } from "../models/models.ts";

export class ValoracionPromediodeEstudianteGetAdapter {
    name: string;
    student_id: string;
    teacher_name: string;
    teacher_valoration: number | null;

    constructor(data: ValoracionPromediodeEstudianteGetDB) {
        this.name = data.name;
        this.student_id = data.student_id;
        this.teacher_name = data.teacher_name;
        this.teacher_valoration = data.teacher_valoration;
    }
    [key: string]: string | number | null;
}