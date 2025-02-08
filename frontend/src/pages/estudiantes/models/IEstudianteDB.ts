import {ICursoGetDB} from "../../cursos/models/ICursoGetDB.ts";

export interface IEstudianteDB {
    id: string,
    name: string,
    lastname: string,
    age: number,
    email: string,
    extra_activities: boolean,
    username: string,
    course: ICursoGetDB,
}