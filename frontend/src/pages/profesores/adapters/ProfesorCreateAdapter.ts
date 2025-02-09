import {ProfesorCreateDB} from "../models/ProfesorCreateDB.ts";

export class ProfesorCreateAdapter {
    static Properties = ['Nombre', 'Apellidos', 'Especialidad', 'Contrato', 'Experiencia', 'Correo' ,  'Usuario',  'Salario'  , 'Asignaturas']
    name: string
    lastname: string
    email: string
    specialty: string
    contractType: string
    experience: number
    salary : number
    username: string
    subjects: string[]

    constructor(profesorCreateDB: ProfesorCreateDB) {

        this.name = profesorCreateDB.name;
        this.lastname = profesorCreateDB.lastname;
        this.email = profesorCreateDB.email;
        this.specialty = profesorCreateDB.specialty;
        this.contractType = profesorCreateDB.contract_type;
        this.experience = profesorCreateDB.experience;
        this.username = profesorCreateDB.username;
        this.salary = profesorCreateDB.salary;
        this.subjects = profesorCreateDB.subjects;
    }

}