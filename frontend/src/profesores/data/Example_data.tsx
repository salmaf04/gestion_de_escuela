import {ProfesorGet} from "../models/ProfesorGetDB.ts";

export const dataExample: ProfesorGet[] =
    [
        {
            id: "1",
            name: "Juan",
            fullname: "Perez",
            specialty: "Matematicas",
            contract_type: "Temporal",
            experience: 3,
            email: "juan@email.com",
            username: "juan",
            list_of_subjects: ["Matematicas", "Fisica"],
            valoration: "4.5"
        },
        {
            id: "2",
            name: "Pedro",
            fullname: "Gomez",
            specialty: "Fisica",
            contract_type: "Temporal",
            experience: 5,
            email: "pedro@email.com",
            username: "pedro",
            list_of_subjects: ["Fisica", "Quimica"],
            valoration: "4.5"
        },
        {
            id: "3",
            name: "Maria",
            fullname: "Lopez",
            specialty: "Quimica",
            contract_type: "Temporal",
            experience: 2,
            email: "maria@email.com",
            username: "maria",
            list_of_subjects: ["Quimica", "Biologia"],
            valoration: "4.5"
        }
    ]
