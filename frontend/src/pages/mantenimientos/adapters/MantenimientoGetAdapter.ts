import {IMantenimientoLocal} from "../models/IMantenimientoLocal.ts";
import {IMantenimientoDB} from "../models/IMantenimientoDB.ts";
import {MedioGetDB} from "../../medios/models/MedioGetDB.ts";

export class MantenimientoGetAdapter implements IMantenimientoLocal {
    static Properties = ['Id', 'Medio', 'Fecha', 'Costo', "Finalizado"]
    id: string
    mean: MedioGetDB;
    date: string;
    cost: number;
    finished: boolean

    constructor(mantenimientoDB: IMantenimientoDB) {
        this.id = mantenimientoDB.id;
        this.mean = mantenimientoDB.mean;
        this.date = mantenimientoDB.date;
        this.cost = mantenimientoDB.cost;
        this.finished = mantenimientoDB.finished
    }

}