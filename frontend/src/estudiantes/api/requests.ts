import { EstudianteGetResponse } from "../models/EstudianteGetDB.ts";
import { EstudianteCreateAdapter } from "../adapters/EstudianteCreateAdapter.ts";
import { EstudianteCreateDB } from "../models/EstudianteCreateDB.ts";

export function postEstudiante(estudiante: EstudianteCreateAdapter) {
    const estudianteDB: EstudianteCreateDB = {
        name: estudiante.name,
        age: estudiante.age,
        email: estudiante.email,
        extra_activities: estudiante.extraActivities,
        username: estudiante.username,
        password: estudiante.password
    }
    return fetch('http://localhost:8000/student/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify(estudianteDB),
    })
}

export function patchEstudiante(id: string, estudiante: EstudianteCreateAdapter) {
    const estudianteDB: EstudianteCreateDB = {
        name: estudiante.name,
        age: estudiante.age,
        email: estudiante.email,
        extra_activities: estudiante.extraActivities,
        username: estudiante.username,
        password: estudiante.password
    }
    return fetch(`http://localhost:8000/student/${id}`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify(estudianteDB),
    });
}

export async function getEstudiantes(): Promise<EstudianteGetResponse> {
    return await fetch('http://localhost:8000/student/', {
            headers: {
                'Authorization': `Bearer ${sessionStorage.getItem('token')}`
            }
        }
        ).then(res => res.json() as Promise<EstudianteGetResponse>)
}

export function deleteEstudiante(id: string) {
    return fetch(`http://localhost:8000/student/${id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}