import {CostoPromedioGetDB} from "../models/models.ts";

export class CostoPromedioGetAdapter {
    average_cost: string;
    mean_id: string;
    mean_name: string;

    constructor(data: CostoPromedioGetDB) {
        this.average_cost = data.average_cost;
        this.mean_id = data.mean_id;
        this.mean_name = data.mean_name;
    }
    [key: string]: string | number;
}