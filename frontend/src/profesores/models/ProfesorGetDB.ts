import {IApiObject} from "../../api/IApiObject.ts";

export interface ProfesorDB extends IApiObject{
        id: string
        name: string
        fullname: string
        specialty: string
        contract_type: string
        experience: number
        email: string
        username: string
        list_of_subjects: string[]
        valoration: string
    }

export type ProfesorGetResponse = ProfesorDB[]