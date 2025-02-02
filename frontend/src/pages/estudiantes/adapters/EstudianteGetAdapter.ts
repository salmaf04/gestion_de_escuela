import { IEstudianteDB } from "../models/IEstudianteDB.ts";
import {ICursoGetDB} from "../../cursos/models/ICursoGetDB.ts";

export class EstudianteGetAdapter{
    static Properties = ['Id', 'Nombre', 'Apellidos', 'Edad', 'Correo', 'ActividadesExtra', 'Usuario', "Curso"]
    id: string;
    lastname: string
    name: string;
    age: number;
    email: string;
    extra_activities: boolean;
    username: string;
    course: ICursoGetDB;

    constructor(estudianteGetDB: IEstudianteDB, curso: ICursoGetDB) {
        this.id = estudianteGetDB.id;
        this.name = estudianteGetDB.name;
        this.age = estudianteGetDB.age;
        this.email = estudianteGetDB.email;
        this.username = estudianteGetDB.username;
        this.extra_activities = estudianteGetDB.extra_activities;
        this.course = curso;
        this.lastname = estudianteGetDB.lastname
    }


}