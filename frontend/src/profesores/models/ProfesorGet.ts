import {DBObject} from "../../types.ts";

export class ProfesorGet implements DBObject{
    static Properties = ['Id', 'Nombre', 'Apellidos', 'Especialidad', 'Contrato', 'Experiencia', 'Correo', 'Usuario', 'Asignaturas', 'Valoracion']
    id: string
    "name": string
    "fullname": string
    "specialty": string
    "contract_type": string
    "experience": number
    "email": string
    "username": string
    "list_of_subjects": string[]
    "valoration": string

    constructor(Id: string, Nombre: string, Apellidos: string, Usuario: string, Especialidad: string, Contrato: string, Experiencia: number, Correo: string, Asignaturas: string[], Valoracion: string) {
        this.id = Id;
        this.name = Nombre;
        this.fullname = Apellidos;
        this.specialty = Especialidad;
        this.contract_type = Contrato;
        this.experience = Experiencia;
        this.email = Correo;
        this.username = Usuario;
        this.list_of_subjects = Asignaturas;
        this.valoration = Valoracion;
    }
}