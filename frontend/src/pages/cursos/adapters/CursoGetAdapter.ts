import {ICursoGetDB} from "../models/ICursoGetDB.ts";

export class CursoGetAdapter {
    static Properties = ['ID' , 'Año de inicio', 'Año de Fin']
    id: string;
    start_year: number ;
    end_year: number ;

    constructor(cursoGetDB: ICursoGetDB) {
        this.id = cursoGetDB.id;
        this.start_year = cursoGetDB.start_year;
        this.end_year = cursoGetDB.end_year;
    }
}