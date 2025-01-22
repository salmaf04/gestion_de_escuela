import { NotaGetDB } from "../models/NotaGetDB.ts";

export class NotaGetAdapter {
    static Properties = ['Profesor', 'Estudiante', 'Asignatura', 'Nota'];
    id: string;
    teacher_id: string;
    student_id: string;
    subject_id: string;
    note_value: number;

    constructor(notaCreateDB: NotaGetDB) {
        this.id = notaCreateDB.id;
        this.teacher_id = notaCreateDB.teacher_id;
        this.student_id = notaCreateDB.student_id;
        this.subject_id = notaCreateDB.subject_id;
        this.note_value = notaCreateDB.note_value;
    }
}