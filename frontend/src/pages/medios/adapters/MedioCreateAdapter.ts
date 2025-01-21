import { MedioCreateDB } from "../models/MedioCreateDB.ts";

export class MedioCreateAdapter {
    name: string;
    state: string;
    location: string;
    classroom_id: string;
    type: string;

    constructor(medioCreateDB: MedioCreateDB) {
        this.name = medioCreateDB.name;
        this.state = medioCreateDB.state;
        this.location = medioCreateDB.location;
        this.classroom_id = medioCreateDB.classroom_id;
        this.type = medioCreateDB.type;
    }
}