import { MedioCreateDB } from "../models/MedioCreateDB.ts";
import { MedioCreateAdapter } from "../adapters/MedioCreateAdapter.ts";

export function getMedioCreateDbFromAdapter(medioAdapter: MedioCreateAdapter): MedioCreateDB {
    return {
        name: medioAdapter.name,
        state: medioAdapter.state,
        location: medioAdapter.location,
        classroom_id: medioAdapter.classroom_id,
        type: medioAdapter.type
    };
}