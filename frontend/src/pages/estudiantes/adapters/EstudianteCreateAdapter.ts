import { EstudianteCreateDB } from "../models/EstudianteCreateDB.ts";

export class EstudianteCreateAdapter {
    static Properties = ['Nombre', 'Edad', 'Correo', 'ActividadesExtra', 'Usuario', 'Contraseña']
    name: string;
    age: number;
    email: string;
    extraActivities: boolean;
    username: string;
    password: string;

    constructor(estudianteCreateDB: EstudianteCreateDB) {
        this.name = estudianteCreateDB.name;
        this.age = estudianteCreateDB.age;
        this.email = estudianteCreateDB.email;
        this.extraActivities = estudianteCreateDB.extra_activities;
        this.username = estudianteCreateDB.username;
        this.password = estudianteCreateDB.password;
    }
}