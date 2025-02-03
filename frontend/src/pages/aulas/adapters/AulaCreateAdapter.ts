import { AulaCreateDB } from "../models/AulaCreateDB.ts";

export class AulaCreateAdapter {
    number: number
    location: string;
    capacity: number;

    constructor(aulaCreateDB: AulaCreateDB) {
        this.number = aulaCreateDB.number;
        this.location = aulaCreateDB.location;
        this.capacity = aulaCreateDB.capacity;
    }
}