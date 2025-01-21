import { EstudianteGetDB } from "../models/EstudianteGetDB.ts";

export class EstudianteGetAdapter {
    static Properties = ['Id', 'Nombre', 'Edad', 'Correo', 'ActividadesExtra', 'Usuario', 'Contraseña']
    id: string;
    name: string;
    age: number;
    email: string;
    extraActivities: boolean;
    username: string;
    password: string;

    constructor(estudianteGetDB: EstudianteGetDB) {
        this.id = estudianteGetDB.id;
        this.name = estudianteGetDB.name;
        this.age = estudianteGetDB.age;
        this.email = estudianteGetDB.email;
        this.extraActivities = estudianteGetDB.extra_activities;
        this.username = estudianteGetDB.username;
        this.password = estudianteGetDB.password;
    }
}