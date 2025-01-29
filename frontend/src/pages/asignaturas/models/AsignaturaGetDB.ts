export type AsignaturaGetDB = {

    id : string;
    name: string;
    hourly_load: number;
    study_program: number;
    classroom_id: string;
    course_id: string
}

export type AsignaturaGetResponse = AsignaturaGetDB[]