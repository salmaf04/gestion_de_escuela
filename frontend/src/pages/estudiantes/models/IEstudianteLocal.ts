import {ICursoGetDB} from "../../cursos/models/ICursoGetDB.ts";

export interface IEstudianteLocal {
    id: string,
    name: string,
    age: number,
    email: string,
    extra_activities: boolean,
    username: string,
    password: string
    course_year: number,
    course: ICursoGetDB,
}