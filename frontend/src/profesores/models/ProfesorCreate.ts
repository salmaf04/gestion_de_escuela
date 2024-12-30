export class ProfesorCreate{
    static Properties = ['Nombre', 'Apellidos', 'Especialidad', 'Contrato', 'Experiencia', 'Correo', 'Usuario', 'Asignaturas']
    "name": string
    "fullname": string
    "specialty": string
    "contract_type": string
    "experience": number
    "email": string
    "username": string
    "list_of_subjects": string[]


    constructor(Nombre: string, Apellidos: string, Usuario: string, Especialidad: string, Contrato: string, Experiencia: number, Correo: string, Asignaturas: string[]) {
        this.name = Nombre;
        this.fullname = Apellidos;
        this.specialty = Especialidad;
        this.contract_type = Contrato;
        this.experience = Experiencia;
        this.email = Correo;
        this.username = Usuario;
        this.list_of_subjects = Asignaturas;
    }
}