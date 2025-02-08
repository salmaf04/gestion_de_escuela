import {AsignaturaGetDB} from "../../asignaturas/models/AsignaturaGetDB.ts";

export type ProfesorDB = {

        id: string
        "name": string
        "lastname": string
        "specialty": string
        "contract_type": string
        "experience": number
        "salary" : number,
        "email": string
        "username": string
        "subjects": AsignaturaGetDB[]
        "valoration": number,
        alert: number
    }

export type ProfesorGetResponse = ProfesorDB[]