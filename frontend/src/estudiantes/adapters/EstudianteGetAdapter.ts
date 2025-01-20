import {DBObject} from "../../types.ts";
import {EstudianteDB} from "../models/EstudianteGetResponse.ts";

export class EstudianteGetAdapter implements DBObject{
    static Properties = ['Id', 'Nombre', 'Apellidos', 'Especialidad', 'Contrato', 'Experiencia', 'Correo', 'Usuario', 'Estudiantes', 'Valoracion']
    id: string
    name: string
    lastname: string
    specialty: string
    contractType: string
    experience: number
    email: string
    username: string
    estudiantes: string[]
    valoracion: string

    constructor(estudianteModel: EstudianteDB) {
        this.id = estudianteModel.id;
        this.name = estudianteModel.name;
        this.lastname = estudianteModel.fullname;
        this.specialty = estudianteModel.specialty;
        this.contractType = estudianteModel.contract_type;
        this.experience = estudianteModel.experience;
        this.email = estudianteModel.email;
        this.username = estudianteModel.username;
        this.estudiantes = estudianteModel.list_of_subjects;
        this.valoracion = estudianteModel.valoration;
    }
}