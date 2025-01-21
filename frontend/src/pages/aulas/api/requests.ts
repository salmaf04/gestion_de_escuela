import {AulaCreateAdapter} from "../adapters/MedioCreateAdapter.ts";
import {AulaCreateDto} from "../models/MedioCreateDto.ts";


function postAula(aula: AulaCreateAdapter) {

    const aulaDB: AulaCreateDto = {
        name: aula.name,
        fullname: aula.lastname,
        email: aula.email,
        specialty: aula.specialty,
        contract_type: aula.contractType,
        experience: aula.experience,
        username: aula.username,
        //TODO Agregar las aulas
        list_of_subjects: ['asdsad']
    }

    console.log(aulaDB)
    return fetch('http://localhost:8000/subject/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify({
            ...aulaDB,
            "password": aulaDB.username
        }),
    })
}

function getAulas() {
    return fetch('http://localhost:8000/subject/', {
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}

function putAula(aula: AulaCreateAdapter) {
    const aulaDB: AulaCreateDto = {
        name: aula.name,
        fullname: aula.lastname,
        email: aula.email,
        specialty: aula.specialty,
        contract_type: aula.contractType,
        experience: aula.experience,
        username: aula.username,
        list_of_subjects: aula.aulas
    }
    //todo revisar metodo
    return fetch('http://localhost:8000/subject/', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify({
            ...aulaDB,
            "password": aulaDB.username
        }),
    })
}

function deleteAula(id: string) {
    return fetch(`http://localhost:8000/subject/${id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}

export default {postAula, getAulas, putAula, deleteAula}