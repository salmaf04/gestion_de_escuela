import {ProfesorCreate, ProfesorGet} from "../dto/types.ts";

export function postProfesor(profesor: ProfesorCreate) {
    return fetch('http://localhost:8000/teacher/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            ...profesor,
            "password": profesor.username
        }),
    })
}

export async function getProfesores(): Promise<Array<ProfesorGet>> {
    return await fetch('http://localhost:8000/teacher/').then(res => res.json() as Promise<Array<ProfesorGet>>)
}
