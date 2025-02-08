import {ProfesorGetResponse} from "../models/ProfesorGetDB.ts";
import {ProfesorGetAdapter} from "../adapters/ProfesorGetAdapter.ts";
import {ProfesorCreateDB} from "../models/ProfesorCreateDB.ts";
import {ProfesorCreateAdapter} from "../adapters/ProfesorCreateAdapter.ts";

export function getProfesorFromResponse(profesorResponse: ProfesorGetResponse) {
    const profesores: ProfesorGetAdapter[] = []
    for (const key in profesorResponse) {
        const profesor = profesorResponse[key]
        profesores.push(new ProfesorGetAdapter(profesor))
    }
    return profesores
}


export function getProfesorCreateDbFromAdapter(profesorAdapter: ProfesorCreateAdapter): ProfesorCreateDB {
    return {
        name: profesorAdapter.name,
        lastname: profesorAdapter.lastname,
        email: profesorAdapter.email,
        specialty: profesorAdapter.specialty,
        contract_type: profesorAdapter.contractType,
        experience: profesorAdapter.experience,
        username: profesorAdapter.username,
        subjects: profesorAdapter.subjects,
        salary: profesorAdapter.salary
    }
}

export function getTextEllipsis(text?: string, length: number = 10): string {
    if (text?.split(" ").length === 1) {
        return text ? text.length > length ? text.slice(0, length) + '...' : text : ""
    }
    return text ?? ""
}