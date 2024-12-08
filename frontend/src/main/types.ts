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
export type Profesor = {
    Nombre: string;
    Apellidos: string;
    Contrato: string;
    Asignaturas: string;
    Valoracion: string;
    Especialidad: string;
    Experiencia: string

}