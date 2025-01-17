import {ProfesorDB} from "../../profesores/models/ProfesorGetDB.ts";

export type EstudianteGetDB = {
    "name": "string",
    "age": number,
    "email": "string",
    "extra_activities": boolean,
    "username": "string",
    "password": "string"
}

export type EstudianteGetResponse = {
    [index: string]: EstudianteGetDB
}