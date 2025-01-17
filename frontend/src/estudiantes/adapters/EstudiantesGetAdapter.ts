import { DBObject } from "../../types.ts";
import {EstudianteGetDB} from "../models/EstudianteGetDB.ts";

export class EstudiantesGetAdapter implements DBObject {
    static Properties = ['Id', 'Nombre', 'Edad', 'Correo', 'ActividadesExtra', 'Usuario', 'Contraseña']
    id: string
    name: string
    age: number
    email: string
    extraActivities: boolean
    username: string
    password: string

    constructor(estudiantesModel: EstudianteGetDB) {
        this.id = estudiantesModel.id;
        this.name = estudiantesModel.name;
        this.age = estudiantesModel.age;
        this.email = estudiantesModel.email;
        this.extraActivities = estudiantesModel.extra_activities;
        this.username = estudiantesModel.username;
        this.password = estudiantesModel.password;
    }
}