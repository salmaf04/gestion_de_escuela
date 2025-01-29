import {CostoPromedioGetDB} from "../models/models.ts";

export class CostoPromedioGetAdapter {
    average_cost: string;
    mean_id: string;
    mean_name: string;

    constructor(costoPromedio: CostoPromedioGetDB) {
        this.average_cost = costoPromedio.average_cost;
        this.mean_id = costoPromedio.mean_id;
        this.mean_name = costoPromedio.mean_name;
    }
    [key: string]: string;
}
