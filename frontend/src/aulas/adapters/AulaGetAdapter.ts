import {DBObject} from "../../types.ts";
import {AulaDB} from "../models/MedioGetResponse.ts";

export class AulaGetAdapter implements DBObject{
    static Properties = ['Id', 'Nombre', 'Apellidos', 'Especialidad', 'Contrato', 'Experiencia', 'Correo', 'Usuario', 'Aulas', 'Valoracion']
    id: string
    name: string
    lastname: string
    specialty: string
    contractType: string
    experience: number
    email: string
    username: string
    aulas: string[]
    valoracion: string

    constructor(aulaModel: AulaDB) {
        this.id = aulaModel.id;
        this.name = aulaModel.name;
        this.lastname = aulaModel.fullname;
        this.specialty = aulaModel.specialty;
        this.contractType = aulaModel.contract_type;
        this.experience = aulaModel.experience;
        this.email = aulaModel.email;
        this.username = aulaModel.username;
        this.aulas = aulaModel.list_of_subjects;
        this.valoracion = aulaModel.valoration;
    }
}