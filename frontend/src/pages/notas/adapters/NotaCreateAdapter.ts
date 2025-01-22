import { NotaCreateDB } from "../models/NotaCreateDB.ts";

export class NotaCreateAdapter {
    static Properties = ['Profesor_id', 'Estudiante_id', 'Asignatura_id', 'Valor_Nota'];
    teacher_id: string;
    student_id: string;
    subject_id: string;
    note_value: number;

    constructor(notaCreateDB: NotaCreateDB) {
        this.teacher_id = notaCreateDB.teacher_id;
        this.student_id = notaCreateDB.student_id;
        this.subject_id = notaCreateDB.subject_id;
        this.note_value = notaCreateDB.note_value;
    }
}