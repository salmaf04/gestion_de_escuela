import { AsignaturaCreateDB } from "../models/AsignaturaCreateDB.ts";
import { AsignaturaCreateAdapter } from "../adapters/AsignaturaCreateAdapter.ts";

export function getAsignaturaCreateDbFromAdapter(asignaturaAdapter: AsignaturaCreateAdapter): AsignaturaCreateDB {
    return {
        name: asignaturaAdapter.name,
        hourly_load: asignaturaAdapter.hourly_load,
        study_program: asignaturaAdapter.study_program,
        classroom_id: asignaturaAdapter.classroom_id,
    };
}