import {MantenimientoCreateAdapter} from "../adapters/MantenimientoCreateAdapter.ts";
import {MantenimientoCreateDto} from "../models/MantenimientoCreateDto.ts";


function postMantenimiento(mantenimiento: MantenimientoCreateAdapter) {

    const mantenimientoDB: MantenimientoCreateDto = {
        name: mantenimiento.name,
        fullname: mantenimiento.lastname,
        email: mantenimiento.email,
        specialty: mantenimiento.specialty,
        contract_type: mantenimiento.contractType,
        experience: mantenimiento.experience,
        username: mantenimiento.username,
        //TODO Agregar las mantenimientos
        list_of_subjects: ['asdsad']
    }

    console.log(mantenimientoDB)
    return fetch('http://localhost:8000/subject/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify({
            ...mantenimientoDB,
            "password": mantenimientoDB.username
        }),
    })
}

function getMantenimientos() {
    return fetch('http://localhost:8000/subject/', {
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}

function putMantenimiento(mantenimiento: MantenimientoCreateAdapter) {
    const mantenimientoDB: MantenimientoCreateDto = {
        name: mantenimiento.name,
        fullname: mantenimiento.lastname,
        email: mantenimiento.email,
        specialty: mantenimiento.specialty,
        contract_type: mantenimiento.contractType,
        experience: mantenimiento.experience,
        username: mantenimiento.username,
        list_of_subjects: mantenimiento.mantenimientos
    }
    //todo revisar metodo
    return fetch('http://localhost:8000/subject/', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify({
            ...mantenimientoDB,
            "password": mantenimientoDB.username
        }),
    })
}

function deleteMantenimiento(id: string) {
    return fetch(`http://localhost:8000/subject/${id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}

export default {postMantenimiento, getMantenimientos, putMantenimiento, deleteMantenimiento}