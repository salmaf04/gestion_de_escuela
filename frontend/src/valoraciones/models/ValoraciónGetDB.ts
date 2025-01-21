export type ValoracionGetDB = {
    id : string ;
    teacher_id: string;
    student_id: string;
    subject_id: string;
    course_id: string;
    grade: number;
};

export type ValoracionGetResponse = {
    [index: string]: ValoracionGetDB
}