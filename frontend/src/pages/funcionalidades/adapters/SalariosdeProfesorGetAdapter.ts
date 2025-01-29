import { SalariosdeProfesoresGetDB } from "../models/models.ts";

export class SalariosdeProfesoresGetAdapter {
    name: string;
    valorations: number[];
    date: string;
    means: boolean;

    constructor(data: SalariosdeProfesoresGetDB) {
        this.name = data.name;
        this.valorations = data.valorations;
        this.date = data.date;
        this.means = data.means;
    }
}