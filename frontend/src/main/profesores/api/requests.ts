import {Profesor} from "../../types.ts";

export function postProfesor(profesor: Profesor) {
    return fetch('http://localhost:8000/teacher/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(
            {
                "name": profesor.Nombre,
                "fullname": profesor.Apellidos,
                "username": profesor.Usuario,
                "specialty": profesor.Especialidad,
                "contract_type": profesor.Contrato,
                "experience": profesor.Experiencia,
                "email": `${profesor.Nombre}${profesor.Apellidos}${(Math.random() % 100).toString()}@gmail.com`,
                "password": profesor.Password
            }
        ),
    })
}
