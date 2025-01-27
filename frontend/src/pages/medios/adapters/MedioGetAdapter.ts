import { MedioGetDB } from "../models/MedioGetDB.ts";

export class MedioGetAdapter {
    static Properties = ['Id', 'Nombre', 'Estado', 'Ubicación', 'Id del aula', 'Tipo']
    id: string;
    name: string;
    state: string;
    location: string;
    classroom_id: string;
    type: string;

    constructor(medioGetDB: MedioGetDB) {
        this.id = medioGetDB.id;
        this.name = medioGetDB.name;
        this.state = medioGetDB.state;
        this.location = medioGetDB.location;
        this.classroom_id = medioGetDB.classroom_id;
        this.type = medioGetDB.type;
    }
}