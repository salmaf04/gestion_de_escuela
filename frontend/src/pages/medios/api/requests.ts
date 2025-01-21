import {MedioCreateAdapter} from "../adapters/MedioCreateAdapter.ts";


function postMedio(medio: MedioCreateAdapter) {

    const medioDB: MedioCreateDto = {
        name: medio.name,
        fullname: medio.lastname,
        email: medio.email,
        specialty: medio.specialty,
        contract_type: medio.contractType,
        experience: medio.experience,
        username: medio.username,
        //TODO Agregar las medios
        list_of_subjects: ['asdsad']
    }

    console.log(medioDB)
    return fetch('http://localhost:8000/subject/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify({
            ...medioDB,
            "password": medioDB.username
        }),
    })
}

function getMedios() {
    return fetch('http://localhost:8000/subject/', {
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}

function putMedio(medio: MedioCreateAdapter) {
    const medioDB: MedioCreateDto = {
        name: medio.name,
        fullname: medio.lastname,
        email: medio.email,
        specialty: medio.specialty,
        contract_type: medio.contractType,
        experience: medio.experience,
        username: medio.username,
        list_of_subjects: medio.medios
    }
    //todo revisar metodo
    return fetch('http://localhost:8000/subject/', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify({
            ...medioDB,
            "password": medioDB.username
        }),
    })
}

function deleteMedio(id: string) {
    return fetch(`http://localhost:8000/subject/${id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}

export default {postMedio, getMedios, putMedio, deleteMedio}