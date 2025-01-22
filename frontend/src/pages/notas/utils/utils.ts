import { NotaCreateAdapter } from "../adapters/NotaCreateAdapter.ts";
import { NotaCreateDB } from "../models/NotaCreateDB.ts";

export const getNotaCreateDbFromAdapter = (nota: NotaCreateAdapter): NotaCreateDB => {
    return {
        student_id: nota.student_id,
        subject_id: nota.subject_id,
        note_value: nota.note_value
    };
};