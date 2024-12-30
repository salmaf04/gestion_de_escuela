import {ProfesorCreate, ProfesorGet} from "../dto/types.ts";

export function postProfesor(profesor: ProfesorCreate) {
    return fetch('http://localhost:8000/teacher/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify({
            ...profesor,
            "password": profesor.username
        }),
    })
}

export async function getProfesores(): Promise<Array<ProfesorGet>> {
    return await fetch('http://localhost:8000/teacher/', {
            headers: {
                'Authorization': `Bearer ${sessionStorage.getItem('token')}`
            }
        }
        ).then(res => res.json() as Promise<Array<ProfesorGet>>)
}

export function deleteProfesor(id: string) {
    return fetch(`http://localhost:8000/teacher/${id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}