import { EstudianteGetResponse } from "../models/EstudianteGetDB.ts";
import { EstudianteGetAdapter } from "../adapters/EstudianteGetAdapter.ts";

export function getEstudianteFromResponse(estudianteResponse: EstudianteGetResponse) {
    const estudiantes: EstudianteGetAdapter[] = [];
    for (const key in estudianteResponse) {
        const estudiante = estudianteResponse[key];
        estudiantes.push(new EstudianteGetAdapter(estudiante));
    }
    return estudiantes;
}