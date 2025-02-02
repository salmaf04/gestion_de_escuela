import {ProfesorCreateDB} from "../models/ProfesorCreateDB.ts";
import {ProfesorGetAdapter} from "./ProfesorGetAdapter.ts";

export class ProfesorCreateAdapter implements Partial<ProfesorGetAdapter>{
    static Properties = ['Nombre', 'Apellidos', 'Especialidad', 'Contrato', 'Experiencia', 'Salario' ,  'Correo', 'Usuario', 'Asignaturas']
    name: string
    lastname: string
    email: string
    specialty: string
    contractType: string
    experience: number
    salary : number
    username: string
    asignaturas: string[]

    constructor(profesorCreateDB: ProfesorCreateDB) {

        this.name = profesorCreateDB.name;
        this.lastname = profesorCreateDB.lastname;
        this.email = profesorCreateDB.email;
        this.specialty = profesorCreateDB.specialty;
        this.contractType = profesorCreateDB.contract_type;
        this.experience = profesorCreateDB.experience;
        this.username = profesorCreateDB.username;
        this.salary = profesorCreateDB.salary;
        this.asignaturas = profesorCreateDB.list_of_subjects;
    }

}