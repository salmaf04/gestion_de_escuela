import { ProfesorEspGetDB } from '../models/models.ts';

export class ProfesorEspGetAdapter {
    id: string;
    name: string;
    specialty: string;
    mean: string;
    state: string;

    constructor(profesor: ProfesorEspGetDB) {
        this.id = profesor.id;
        this.name = profesor.name;
        this.specialty = profesor.specialty;
        this.mean = profesor.mean;
        this.state = profesor.state;
    }
    [key: string]: string;
}

