import {EstudianteCreateAdapter} from "../adapters/EstudianteCreateAdapter.ts";
import {EstudianteCreateDB} from "../models/EstudianteCreateDB.ts";

export function getEstudianteCreateDbFromAdapter(estudiante: EstudianteCreateAdapter): EstudianteCreateDB{
    return {
        age: estudiante.age,
        email: estudiante.email,
        name: estudiante.name,
        password: estudiante.password,
        username: estudiante.username,
        extra_activities: estudiante.extraActivities,
    }
}