import { ProfesorGetResponse} from "../models/ProfesorGetDB.ts";
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


export function getProfesorCreateDbFromAdapter(profesorAdapter: ProfesorCreateAdapter): ProfesorCreateDB{
    return {
        name: profesorAdapter.name,
        fullname: profesorAdapter.lastname,
        email: profesorAdapter.email,
        specialty: profesorAdapter.specialty,
        contract_type: profesorAdapter.contractType,
        experience: profesorAdapter.experience,
        username: profesorAdapter.username,
        list_of_subjects: profesorAdapter.asignaturas,
        salary: profesorAdapter.salary
    }
}