import {DBObject} from "../../types.ts";
import {MantenimientoDB} from "../models/MantenimientoGetResponse.ts";

export class MantenimientoGetAdapter implements DBObject{
    static Properties = ['Id', 'Nombre', 'Apellidos', 'Especialidad', 'Contrato', 'Experiencia', 'Correo', 'Usuario', 'Mantenimientos', 'Valoracion']
    id: string
    name: string
    lastname: string
    specialty: string
    contractType: string
    experience: number
    email: string
    username: string
    mantenimientos: string[]
    valoracion: string

    constructor(mantenimientoModel: MantenimientoDB) {
        this.id = mantenimientoModel.id;
        this.name = mantenimientoModel.name;
        this.lastname = mantenimientoModel.fullname;
        this.specialty = mantenimientoModel.specialty;
        this.contractType = mantenimientoModel.contract_type;
        this.experience = mantenimientoModel.experience;
        this.email = mantenimientoModel.email;
        this.username = mantenimientoModel.username;
        this.mantenimientos = mantenimientoModel.list_of_subjects;
        this.valoracion = mantenimientoModel.valoration;
    }
}