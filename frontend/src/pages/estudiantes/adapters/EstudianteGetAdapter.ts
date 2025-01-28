import { IEstudianteDB } from "../models/IEstudianteDB.ts";
import {IEstudianteLocal} from "../models/IEstudianteLocal.ts";
import {ICursoGetDB} from "../../cursos/models/ICursoGetDB.ts";

export class EstudianteGetAdapter implements IEstudianteLocal{
    static Properties = ['Id', 'Nombre', 'Edad', 'Correo', 'ActividadesExtra', 'Usuario', 'Contraseña']
    id: string;
    name: string;
    age: number;
    email: string;
    extra_activities: boolean;
    username: string;
    password: string;
    course_year: number;
    course: ICursoGetDB;

    constructor(estudianteGetDB: IEstudianteDB, curso: ICursoGetDB) {
        this.id = estudianteGetDB.id;
        this.name = estudianteGetDB.name;
        this.age = estudianteGetDB.age;
        this.email = estudianteGetDB.email;
        this.username = estudianteGetDB.username;
        this.password = estudianteGetDB.password;
        this.extra_activities = estudianteGetDB.extra_activities;
        this.course_year = estudianteGetDB.course_year;
        this.course = curso;
    }

}