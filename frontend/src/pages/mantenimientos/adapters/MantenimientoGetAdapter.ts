import {IMantenimientoLocal} from "../models/IMantenimientoLocal.ts";
import { MedioGetAdapter } from "../../medios/adapters/MedioGetAdapter.ts";
import {IMantenimientoDB} from "../models/IMantenimientoDB.ts";

export class MantenimientoGetAdapter implements IMantenimientoLocal {
    static Properties = ['Id', 'Medio', 'Fecha', 'Costo']
    id: string
    mean: MedioGetAdapter;
    date: string;
    cost: number;

    constructor(mantenimientoDB: IMantenimientoDB, medio: MedioGetAdapter) {
        this.id = mantenimientoDB.id;
        this.mean = medio;
        this.date = mantenimientoDB.date;
        this.cost = mantenimientoDB.cost;
    }

}