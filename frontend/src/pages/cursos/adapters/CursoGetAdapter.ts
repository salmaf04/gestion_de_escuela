import {ICursoGetDB} from "../models/ICursoGetDB.ts";

export class CursoGetAdapter {
    static Properties = ['ID' , 'Año']
    id: string;
    year: number;


    constructor(cursoGetDB: ICursoGetDB) {
        this.id = cursoGetDB.id;
        this.year = cursoGetDB.year
    }
}