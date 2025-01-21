
export type AusenciaGetDB = {
    id : string;
    student_id: string;
    course_id: string;
    subject_id: string;
    absences: number;
};

export type AusenciaGetResponse = {
    [index: string]: AusenciaGetDB
}