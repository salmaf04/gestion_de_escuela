import {ProfesorDB} from "../models/AsignaturaGeDB.ts";

export const dataExample: ProfesorDB[] = Array.from({ length: 30 }, (_, index) => ({
    id: (index + 1).toString(),
    name: `Name${index + 1}`,
    fullname: `Fullname${index + 1}`,
    specialty: `Specialty${index + 1}`,
    contract_type: "Temporal",
    experience: Math.floor(Math.random() * 10) + 1,
    email: `email${index + 1}@example.com`,
    username: `username${index + 1}`,
    list_of_subjects: [`Subject${index + 1}`, `Subject${index + 2}`],
    valoration: (Math.random() * 5).toFixed(1)
}));
