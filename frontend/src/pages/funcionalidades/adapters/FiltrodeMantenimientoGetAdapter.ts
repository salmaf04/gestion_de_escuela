import {FiltrodeMantenimientoGetDB} from "../models/models.ts";

export class FiltrodeMantenimientoGetAdapter {
    number : string;
    other: number;
    teaching_material: number;
    technological_mean: number;
    total_after_two_years : number;

    constructor(data : FiltrodeMantenimientoGetDB) {
        this.number = data.number;
        this.other = data.other;
        this.teaching_material = data.teaching_material;
        this.technological_mean = data.technological_mean;
        this.total_after_two_years = data.total_after_two_years;

    }
    [key: string]: string | number;
}