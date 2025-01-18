import { ProfesorGetResponse} from "../models/ProfesorGetDB.ts";
import {ProfesorGetAdapter} from "../adapters/ProfesorGetAdapter.ts";

export function getProfesorFromResponse(profesorResponse: ProfesorGetResponse) {
    const profesores: ProfesorGetAdapter[] = []
    for (const key in profesorResponse) {
        const profesor = profesorResponse[key]
        profesores.push(new ProfesorGetAdapter(profesor))
    }
    return profesores
}
