export default class ScreenType {
    title: string;
    icon: string;
    screen: JSX.Element;
    constructor(title: string, icon: string, screen: JSX.Element) {
        this.title = title;
        this.icon = icon;
        this.screen = screen;
    }

}
export interface DBObject {
    Id: string;
}

export class Profesor implements DBObject {
    Id: string;
    Nombre: string;
    Apellidos: string;
    Contrato: string;
    Asignaturas: string;
    Valoracion: string;
    Especialidad: string;
    Experiencia: string;

    constructor(Id: string, Nombre: string, Apellidos: string, Contrato: string, Asignaturas: string, Valoracion: string, Especialidad: string, Experiencia: string) {
        this.Id = Id;
        this.Nombre = Nombre;
        this.Apellidos = Apellidos;
        this.Contrato = Contrato;
        this.Asignaturas = Asignaturas;
        this.Valoracion = Valoracion;
        this.Especialidad = Especialidad;
        this.Experiencia = Experiencia;
    }
}