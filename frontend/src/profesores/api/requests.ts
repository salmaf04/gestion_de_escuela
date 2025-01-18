import {ProfesorCreateAdapter} from "../adapters/ProfesorCreateAdapter.ts";
import {ProfesorCreateDB} from "../models/ProfesorCreateDB.ts";

function postProfesor(profesor: ProfesorCreateAdapter) {
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

function getProfesores() {
    return fetch('http://localhost:8000/teacher/', {
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}

function deleteProfesor(id: string) {
    return fetch(`http://localhost:8000/teacher/${id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}

export default {postProfesor, getProfesores, deleteProfesor}