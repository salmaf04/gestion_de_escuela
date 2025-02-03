import {ICursoGetDB} from "../../cursos/models/ICursoGetDB.ts";
import {IUsuarioLocal} from "../../usuarios/models/IUsuarioLocal.ts";

export interface IEstudianteLocal extends IUsuarioLocal{
    id: string,
    name: string,
    lastname: string,
    age: number,
    email: string,
    extra_activities: boolean,
    username: string,
    course: ICursoGetDB,
    lastname: string,
}