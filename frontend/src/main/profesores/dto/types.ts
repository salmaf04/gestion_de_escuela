import {DBObject} from "../../types.ts";

//TODO revisar Asignnaturas y Valoracion (No vienen de la BD)
export class ProfesorGet implements DBObject{
    static Properties = ['Id', 'Nombre', 'Apellidos', 'Especialidad', 'Contrato', 'Experiencia', 'Correo', 'Usuario']
    id: string
    "name": string
    "fullname": string
    "specialty": string
    "contract_type": string
    "experience": number
    "email": string
    "username": string

    constructor(Id: string, Nombre: string, Apellidos: string, Usuario: string, Especialidad: string, Contrato: string, Experiencia: number, Correo: string) {
        this.id = Id;
        this.name = Nombre;
        this.fullname = Apellidos;
        this.specialty = Especialidad;
        this.contract_type = Contrato;
        this.experience = Experiencia;
        this.email = Correo;
        this.username = Usuario;
    }
}

export class ProfesorCreate{
    static Properties = ['Nombre', 'Apellidos', 'Especialidad', 'Contrato', 'Experiencia', 'Correo', 'Usuario']
    "name": string
    "fullname": string
    "specialty": string
    "contract_type": string
    "experience": number
    "email": string
    "username": string

    constructor(Nombre: string, Apellidos: string, Usuario: string, Especialidad: string, Contrato: string, Experiencia: number, Correo: string) {
        this.name = Nombre;
        this.fullname = Apellidos;
        this.specialty = Especialidad;
        this.contract_type = Contrato;
        this.experience = Experiencia;
        this.email = Correo;
        this.username = Usuario;
    }
}
