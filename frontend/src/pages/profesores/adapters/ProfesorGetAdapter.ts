import {DBObject} from "../../../types.ts";
import {ProfesorDB} from "../models/ProfesorGetDB.ts";
import {AsignaturaGetDB} from "../../asignaturas/models/AsignaturaGetDB.ts";

export class ProfesorGetAdapter implements DBObject{
    static Properties = ['Id', 'Nombre', 'Apellidos', 'Especialidad', 'Contrato', 'Experiencia','Salario', 'Correo' ,  'Usuario', 'Asignaturas', 'Valoracion']
    id: string
    name: string
    lastname: string
    specialty: string
    contractType: string
    experience: number
    salary : number
    email: string
    username: string
    subjects: AsignaturaGetDB[]
    valoracion: number
    alert: number


    constructor(profesorModel: ProfesorDB) {
        this.id = profesorModel.id;
        this.name = profesorModel.name;
        this.lastname = profesorModel.lastname;
        this.specialty = profesorModel.specialty;
        this.contractType = profesorModel.contract_type;
        this.experience = profesorModel.experience;
        this.salary = profesorModel.salary
        this.email = profesorModel.email;
        this.username = profesorModel.username;
        this.subjects = profesorModel.subjects;
        this.valoracion = profesorModel.valoration;
        this.alert = profesorModel.alert;
    }

}