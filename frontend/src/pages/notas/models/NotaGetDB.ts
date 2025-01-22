export type NotaGetDB =
    {
        id : string
        teacher_id: string,
        student_id: string,
        subject_id: string,
        note_value: number,
    }

export type NotaGetResponse = {
    [index: string]: NotaGetDB
}