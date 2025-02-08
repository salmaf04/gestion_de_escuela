import { IEstudianteDB } from "../models/IEstudianteDB.ts";
import {IEstudianteLocal} from "../models/IEstudianteLocal.ts";
import {ICursoGetDB} from "../../cursos/models/ICursoGetDB.ts";

export class EstudianteGetAdapter implements IEstudianteLocal{
    static Properties = ['Id', 'Nombre', 'Apellidos', 'Edad', 'Correo', 'ActividadesExtra', 'Usuario', "Curso"]
    id: string;
    name: string;
    lastname: string;
    age: number;
    email: string;
    extra_activities: boolean;
    username: string;
    course: ICursoGetDB;

    constructor(estudianteGetDB: IEstudianteDB) {
        this.id = estudianteGetDB.id;
        this.name = estudianteGetDB.name;
        this.lastname = estudianteGetDB.lastname;
        this.age = estudianteGetDB.age;
        this.email = estudianteGetDB.email;
        this.username = estudianteGetDB.username;
        this.extra_activities = estudianteGetDB.extra_activities;
        this.course = estudianteGetDB.course;
    }

}