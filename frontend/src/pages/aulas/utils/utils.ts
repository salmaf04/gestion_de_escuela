
import { AulaCreateDB } from "../models/AulaCreateDB.ts";
import { AulaCreateAdapter } from "../adapters/AulaCreateAdapter.ts";

export function getAulaCreateDbFromAdapter(aulaAdapter: AulaCreateAdapter): AulaCreateDB {
    return {
        location: aulaAdapter.location,
        capacity: aulaAdapter.capacity
    };
}