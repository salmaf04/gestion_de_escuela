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
        list_of_subjects: ['TODO'],
        salary : profesor.salary
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

function putProfesor(profesor: ProfesorCreateAdapter) {
    const profesorDB: ProfesorCreateDB = {
        name: profesor.name,
        fullname: profesor.lastname,
        email: profesor.email,
        specialty: profesor.specialty,
        contract_type: profesor.contractType,
        experience: profesor.experience,
        username: profesor.username,
        salary : profesor.salary,
        list_of_subjects: profesor.asignaturas
    }
    //todo revisar metodo
    return fetch('http://localhost:8000/teacher/', {
        method: 'PUT',
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

function deleteProfesor(id: string) {
    return fetch(`http://localhost:8000/teacher/${id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}

export default {postProfesor, getProfesores, putProfesor, deleteProfesor}