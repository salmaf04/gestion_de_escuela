import {MedioGetDB} from "../../medios/models/MedioGetDB.ts";

export interface IMantenimientoDB {
    id: string,
    mean: MedioGetDB,
    date: string,
    cost: number
    finished: boolean

}