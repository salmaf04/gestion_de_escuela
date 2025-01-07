import {DBObject} from "../../types.ts";
import {ProfesorDB} from "../models/ProfesorGetDB.ts";

export class ProfesorGetAdapter implements DBObject{
    static Properties = ['Id', 'Nombre', 'Apellidos', 'Especialidad', 'Contrato', 'Experiencia', 'Correo', 'Usuario', 'Asignaturas', 'Valoracion']
    id: string
    name: string
    lastname: string
    specialty: string
    contractType: string
    experience: number
    email: string
    username: string
    asignaturas: string[]
    valoracion: string

    constructor(profesorModel: ProfesorDB) {
        this.id = profesorModel.id;
        this.name = profesorModel.name;
        this.lastname = profesorModel.fullname;
        this.specialty = profesorModel.specialty;
        this.contractType = profesorModel.contract_type;
        this.experience = profesorModel.experience;
        this.email = profesorModel.email;
        this.username = profesorModel.username;
        this.asignaturas = profesorModel.list_of_subjects;
        this.valoracion = profesorModel.valoration;
    }
}