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

export class Estudiante implements DBObject {
    Id: string;
    Nombre: string;
    Edad: string;
    ActividadesExtras: boolean;

    constructor(Id: string, Nombre: string, Edad: string, ActividadesExtras: boolean) {
        this.Id = Id;
        this.Nombre = Nombre;
        this.Edad = Edad;
        this.ActividadesExtras = ActividadesExtras;
    }
}

export class Medio implements DBObject {
    Id: string;
    Nombre: string;
    Estado: string;
    Ubicacion: string;

    constructor(Id: string, Nombre: string, Estado: string, Ubicacion: string) {
        this.Id = Id;
        this.Nombre = Nombre;
        this.Estado = Estado;
        this.Ubicacion = Ubicacion;
    }
}

export class Aula implements DBObject {
    Id: string;
    Ubicacion: string;
    Capacidad: number;

    constructor(Id: string, Ubicacion: string, Capacidad: number) {
        this.Id = Id;
        this.Ubicacion = Ubicacion;
        this.Capacidad = Capacidad;
    }
}

export class MantenimientoDeMedio implements DBObject {
    Id: string;
    Medio: string;
    Fecha: string;
    Costo: string;

    constructor(Id: string, Fecha: string, Medio : string ,  Costo: string) {
        this.Id = Id;
        this.Medio = Medio;
        this.Fecha = Fecha;
        this.Costo = Costo;
    }
}
