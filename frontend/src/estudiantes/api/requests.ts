import { EstudianteCreateAdapter } from "../adapters/EstudianteCreateAdapter.ts";
import { EstudianteCreateDB } from "../models/EstudianteCreateDB.ts";


function postEstudiante(estudiante: EstudianteCreateAdapter) {
    const estudianteDB: EstudianteCreateDB = {
        name: estudiante.name,
        age: estudiante.age,
        email: estudiante.email,
        extra_activities: estudiante.extraActivities,
        username: estudiante.username,
        password: estudiante.password
    };

    return fetch('http://localhost:8000/student/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify(estudianteDB),
    });
}

function getEstudiantes() {
    return fetch('http://localhost:8000/student/', {
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    });
}

function putEstudiante(estudiante: EstudianteCreateAdapter) {
    const estudianteDB: EstudianteCreateDB = {
        name: estudiante.name,
        age: estudiante.age,
        email: estudiante.email,
        extra_activities: estudiante.extraActivities,
        username: estudiante.username,
        password: estudiante.password
    };

    return fetch(`http://localhost:8000/student/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify(estudianteDB),
    });
}

function deleteEstudiante(id: string) {
    return fetch(`http://localhost:8000/student/${id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    });
}

export default { postEstudiante, getEstudiantes, putEstudiante, deleteEstudiante };