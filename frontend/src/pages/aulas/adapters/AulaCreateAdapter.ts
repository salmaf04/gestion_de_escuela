import { AulaCreateDB } from "../models/AulaCreateDB.ts";

export class AulaCreateAdapter {
    location: string;
    capacity: number;

    constructor(aulaCreateDB: AulaCreateDB) {
        this.location = aulaCreateDB.location;
        this.capacity = aulaCreateDB.capacity;
    }
}