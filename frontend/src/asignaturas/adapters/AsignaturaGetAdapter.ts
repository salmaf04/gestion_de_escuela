import {DBObject} from "../../types.ts";
import {AsignaturaDB} from "../models/AsignaturaGetDB.ts";

export class AsignaturaGetAdapter implements DBObject{
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

    constructor(asignaturaModel: AsignaturaDB) {
        this.id = asignaturaModel.id;
        this.name = asignaturaModel.name;
        this.lastname = asignaturaModel.fullname;
        this.specialty = asignaturaModel.specialty;
        this.contractType = asignaturaModel.contract_type;
        this.experience = asignaturaModel.experience;
        this.email = asignaturaModel.email;
        this.username = asignaturaModel.username;
        this.asignaturas = asignaturaModel.list_of_subjects;
        this.valoracion = asignaturaModel.valoration;
    }
}