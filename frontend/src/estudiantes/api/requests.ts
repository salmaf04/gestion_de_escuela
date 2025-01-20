import {EstudianteCreateAdapter} from "../adapters/EstudianteCreateAdapter.ts";
import {EstudianteCreateDto} from "../models/EstudianteCreateDto.ts";


function postEstudiante(estudiante: EstudianteCreateAdapter) {

    const estudianteDB: EstudianteCreateDto = {
        name: estudiante.name,
        fullname: estudiante.lastname,
        email: estudiante.email,
        specialty: estudiante.specialty,
        contract_type: estudiante.contractType,
        experience: estudiante.experience,
        username: estudiante.username,
        //TODO Agregar las estudiantes
        list_of_subjects: ['asdsad']
    }

    console.log(estudianteDB)
    return fetch('http://localhost:8000/subject/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify({
            ...estudianteDB,
            "password": estudianteDB.username
        }),
    })
}

function getEstudiantes() {
    return fetch('http://localhost:8000/subject/', {
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}

function putEstudiante(estudiante: EstudianteCreateAdapter) {
    const estudianteDB: EstudianteCreateDto = {
        name: estudiante.name,
        fullname: estudiante.lastname,
        email: estudiante.email,
        specialty: estudiante.specialty,
        contract_type: estudiante.contractType,
        experience: estudiante.experience,
        username: estudiante.username,
        list_of_subjects: estudiante.estudiantes
    }
    //todo revisar metodo
    return fetch('http://localhost:8000/subject/', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify({
            ...estudianteDB,
            "password": estudianteDB.username
        }),
    })
}

function deleteEstudiante(id: string) {
    return fetch(`http://localhost:8000/subject/${id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}

export default {postEstudiante, getEstudiantes, putEstudiante, deleteEstudiante}