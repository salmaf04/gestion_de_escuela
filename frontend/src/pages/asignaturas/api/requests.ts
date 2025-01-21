import {AsignaturaCreateAdapter} from "../adapters/AsignaturaCreateAdapter.ts";
import {AsignaturaCreateDto} from "../models/AsignaturaCreateDB.ts";


function postAsignatura(asignatura: AsignaturaCreateAdapter) {

    const asignaturaDB: AsignaturaCreateDto = {
        name: asignatura.name,
        fullname: asignatura.lastname,
        email: asignatura.email,
        specialty: asignatura.specialty,
        contract_type: asignatura.contractType,
        experience: asignatura.experience,
        username: asignatura.username,
        //TODO Agregar las asignaturas
        list_of_subjects: ['asdsad']
    }

    console.log(asignaturaDB)
    return fetch('http://localhost:8000/subject/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify({
            ...asignaturaDB,
            "password": asignaturaDB.username
        }),
    })
}

function getAsignaturas() {
    return fetch('http://localhost:8000/subject/', {
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}

function putAsignatura(asignatura: AsignaturaCreateAdapter) {
    const asignaturaDB: AsignaturaCreateDto = {
        name: asignatura.name,
        fullname: asignatura.lastname,
        email: asignatura.email,
        specialty: asignatura.specialty,
        contract_type: asignatura.contractType,
        experience: asignatura.experience,
        username: asignatura.username,
        list_of_subjects: asignatura.asignaturas
    }
    //todo revisar metodo
    return fetch('http://localhost:8000/subject/', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify({
            ...asignaturaDB,
            "password": asignaturaDB.username
        }),
    })
}

function deleteAsignatura(id: string) {
    return fetch(`http://localhost:8000/subject/${id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}

export default {postAsignatura, getAsignaturas, putAsignatura, deleteAsignatura}