import {MedioGetAdapter} from "../../medios/adapters/MedioGetAdapter.ts";

export interface IMantenimientoLocal {
    id: string,
    mean: MedioGetAdapter,
    date: string,
    cost: number,
    finished: boolean
}