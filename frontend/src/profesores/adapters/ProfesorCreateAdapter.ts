import {ProfesorCreateDB} from "../models/ProfesorCreateDB.ts";

export class ProfesorCreateAdapter {
    static Properties = ['Nombre', 'Apellidos', 'Especialidad', 'Contrato', 'Experiencia', 'Correo', 'Usuario', 'Asignaturas']
    name: string
    lastname: string
    email: string
    specialty: string
    contractType: string
    experience: number
    username: string
    asignaturas: string[]

    constructor(profesorCreateDB: ProfesorCreateDB) {
        this.name = profesorCreateDB.name;
        this.lastname = profesorCreateDB.fullname;
        this.email = profesorCreateDB.email;
        this.specialty = profesorCreateDB.specialty;
        this.contractType = profesorCreateDB.contract_type;
        this.experience = profesorCreateDB.experience;
        this.username = profesorCreateDB.username;
        this.asignaturas = profesorCreateDB.list_of_subjects;
    }
}