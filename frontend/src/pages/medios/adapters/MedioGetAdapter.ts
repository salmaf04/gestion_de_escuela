import { MedioGetDB } from "../models/MedioGetDB.ts";
import {AulaGetAdapter} from "../../aulas/adapters/AulaGetAdapter.ts";

export class MedioGetAdapter {
    static Properties = ['Id', 'Nombre', 'Estado', 'Ubicación', 'Aula', 'Tipo']
    id: string;
    name: string;
    state: string;
    location: string;
    classroom: AulaGetAdapter;
    type: string;

    constructor(medioGetDB: MedioGetDB, classroom: AulaGetAdapter) {
        this.id = medioGetDB.id;
        this.name = medioGetDB.name;
        this.state = medioGetDB.state;
        this.location = medioGetDB.location;
        this.classroom = classroom;
        this.type = medioGetDB.type;
    }
}