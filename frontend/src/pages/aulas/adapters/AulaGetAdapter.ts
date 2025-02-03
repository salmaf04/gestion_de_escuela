import { AulaGetDB } from "../models/AulaGetDB.ts";

export class AulaGetAdapter {
    static Properties = ['Id', "Aula", 'Ubicación', 'Capacidad']
    id: string;
    number: string
    location: string;
    capacity: number;

    constructor(aulaGetDB: AulaGetDB) {
        this.id = aulaGetDB.id;
        this.number = "Aula "+aulaGetDB.number;
        this.location = aulaGetDB.location;
        this.capacity = aulaGetDB.capacity;
    }
}