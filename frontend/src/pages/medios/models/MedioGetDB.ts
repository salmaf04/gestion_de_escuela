import {AulaGetDB} from "../../aulas/models/AulaGetDB.ts";

export type MedioGetDB = {
    id : string;
    name: string;
    state: string;
    location: string;
    classroom: AulaGetDB;
    type: string;
    to_be_replaced: boolean
    requested_by: string
};

export type MedioGetResponse = {
    [index: string]: MedioGetDB
}