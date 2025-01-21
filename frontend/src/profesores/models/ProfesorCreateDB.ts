import {IApiObject} from "../../api/IApiObject.ts";

export interface ProfesorCreateDB extends IApiObject{
    name: string
    fullname: string
    email: string
    specialty: string
    contract_type: string
    experience: number
    username: string
    list_of_subjects: string[]
}