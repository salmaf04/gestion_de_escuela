
import {ProfesorGetResponse} from "../models/ProfesorGetDB.ts";
import {ProfesorCreateAdapter} from "../adapters/ProfesorCreateAdapter.ts";
import {ProfesorCreateDB} from "../models/ProfesorCreateDB.ts";

export function postProfesor(profesor: ProfesorCreateAdapter) {
    const profesorDB: ProfesorCreateDB = {
        name: profesor.name,
        fullname: profesor.lastname,
        email: profesor.email,
        specialty: profesor.specialty,
        contract_type: profesor.contractType,
        experience: profesor.experience,
        username: profesor.username,
        list_of_subjects: profesor.asignaturas
    }
    return fetch('http://localhost:8000/teacher/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify({
            ...profesorDB,
            "password": profesorDB.username
        }),
    })
}

export async function getProfesores(): Promise<ProfesorGetResponse> {
    return await fetch('http://localhost:8000/teacher/', {
            headers: {
                'Authorization': `Bearer ${sessionStorage.getItem('token')}`
            }
        }
        ).then(res => res.json() as Promise<ProfesorGetResponse>)
}

export function deleteProfesor(id: string) {
    return fetch(`http://localhost:8000/teacher/${id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}