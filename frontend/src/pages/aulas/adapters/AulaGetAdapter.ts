import { AulaGetDB } from "../models/AulaGetDB.ts";

export class AulaGetAdapter {
    static Properties = ['Id', 'Ubicación', 'Capacidad']
    id: string;
    location: string;
    capacity: number;

    constructor(aulaGetDB: AulaGetDB) {
        this.id = aulaGetDB.id;
        this.location = aulaGetDB.location;
        this.capacity = aulaGetDB.capacity;
    }
}