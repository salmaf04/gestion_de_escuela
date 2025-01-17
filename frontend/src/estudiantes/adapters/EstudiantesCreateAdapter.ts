import { EstudiantesCreateDB } from "../models/EstudiantesCreateDB.ts";

export class EstudiantesCreateAdapter {
    static Properties = ['Nombre', 'Edad', 'Correo', 'ActividadesExtra', 'Usuario', 'Contraseña']
    name: string
    age: number
    email: string
    extraActivities: boolean
    username: string
    password: string

    constructor(estudiantesCreateDB: EstudiantesCreateDB) {
        this.name = estudiantesCreateDB.name;
        this.age = estudiantesCreateDB.age;
        this.email = estudiantesCreateDB.email;
        this.extraActivities = estudiantesCreateDB.extra_activities;
        this.username = estudiantesCreateDB.username;
        this.password = estudiantesCreateDB.password;
    }
}