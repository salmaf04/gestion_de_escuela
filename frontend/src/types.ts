import {RolesEnum} from "./api/RolesEnum.ts";

export default class ScreenType {
    title: string;
    icon: string;
    path: string;
    allowedRoles: RolesEnum[]
    constructor(title: string, icon: string, path: string, allowedRoles: RolesEnum[]) {
        this.title = title;
        this.icon = icon;
        this.path = path;
        this.allowedRoles = allowedRoles
    }

}
export interface DBObject {
    id: string;
}

export class Estudiante implements DBObject {
    id: string;
    Nombre: string;
    Edad: string;
    ActividadesExtras: boolean;

    constructor(id: string, Nombre: string, Edad: string, ActividadesExtras: boolean) {
        this.id = id;
        this.Nombre = Nombre;
        this.Edad = Edad;
        this.ActividadesExtras = ActividadesExtras;
    }
}

export class Medio implements DBObject {
    id: string;
    Nombre: string;
    Estado: string;
    Ubicacion: string;

    constructor(id: string, Nombre: string, Estado: string, Ubicacion: string) {
        this.id = id;
        this.Nombre = Nombre;
        this.Estado = Estado;
        this.Ubicacion = Ubicacion;
    }
}

export class Aula implements DBObject {
    id: string;
    Ubicacion: string;
    Capacidad: number;

    constructor(id: string, Ubicacion: string, Capacidad: number) {
        this.id = id;
        this.Ubicacion = Ubicacion;
        this.Capacidad = Capacidad;
    }
}

export class MantenimientoDeMedio implements DBObject {
    id: string;
    Medio: string;
    Fecha: string;
    Costo: string;

    constructor(id: string, Fecha: string, Medio : string ,  Costo: string) {
        this.id = id;
        this.Medio = Medio;
        this.Fecha = Fecha;
        this.Costo = Costo;
    }
}

