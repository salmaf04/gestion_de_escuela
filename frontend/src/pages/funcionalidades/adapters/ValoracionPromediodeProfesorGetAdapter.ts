// `frontend/src/pages/funcionalidades/adapters/ValoracionPromediodeProfesorGetAdapter.ts`
import { ValoracionPromediodeProfesorGetDB } from "../models/models.ts";

export class ValoracionPromediodeProfesorGetAdapter {
    name: string;
    average_valoration: number;
    subjects: string[];

    constructor(data: ValoracionPromediodeProfesorGetDB) {
        this.name = data.name;
        this.average_valoration = data.average_valoration;
        this.subjects = data.subjects;
    }
    [key : string] : string | number | string[];
}