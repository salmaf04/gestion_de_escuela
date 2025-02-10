import { MedioGetDB } from "../models/MedioGetDB.ts";
import {AulaGetDB} from "../../aulas/models/AulaGetDB.ts";

export class MedioGetAdapter {
    static Properties = ['Id', 'Nombre', 'Estado', 'Ubicación', "Aula", 'Tipo']
    id: string;
    name: string;
    state: string;
    location: string;
    classroom: AulaGetDB;
    type: string;
    to_be_replaced: boolean
    requested_by: string

    constructor(medioGetDB: MedioGetDB) {
        this.id = medioGetDB.id;
        this.name = medioGetDB.name;
        this.state = medioGetDB.state;
        this.location = medioGetDB.location;
        this.classroom = medioGetDB.classroom;
        this.type = medioGetDB.type;
        this.to_be_replaced = medioGetDB.to_be_replaced;
        this.requested_by = medioGetDB.requested_by;
    }
}