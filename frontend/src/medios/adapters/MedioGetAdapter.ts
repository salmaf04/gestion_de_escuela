import {DBObject} from "../../types.ts";
import {MedioDB} from "../models/MedioGetResponse.ts";

export class MedioGetAdapter implements DBObject{
    static Properties = ['Id', 'Nombre', 'Apellidos', 'Especialidad', 'Contrato', 'Experiencia', 'Correo', 'Usuario', 'Medios', 'Valoracion']
    id: string
    name: string
    lastname: string
    specialty: string
    contractType: string
    experience: number
    email: string
    username: string
    medios: string[]
    valoracion: string

    constructor(medioModel: MedioDB) {
        this.id = medioModel.id;
        this.name = medioModel.name;
        this.lastname = medioModel.fullname;
        this.specialty = medioModel.specialty;
        this.contractType = medioModel.contract_type;
        this.experience = medioModel.experience;
        this.email = medioModel.email;
        this.username = medioModel.username;
        this.medios = medioModel.list_of_subjects;
        this.valoracion = medioModel.valoration;
    }
}