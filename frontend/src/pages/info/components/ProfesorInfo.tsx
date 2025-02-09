import {useApiProfesor} from "../../profesores/hooks/useApiProfesor.ts";
import {useContext, useEffect} from "react";
import {AppContext} from "../../../App.tsx";
import UserCard, {UserDataProp} from "./UserCard.tsx";

export default function ProfesorInfo() {
    const {getProfesor, profesor} = useApiProfesor()
    const {personalId} = useContext(AppContext)
    useEffect(() => {
        getProfesor(personalId!)
    }, []);

    const userInfo: UserDataProp[] = [
        {
            name: 'Nombre',
            value: profesor?.name ?? 'No disponible',
        },
        {
            name: 'Apellidos',
            value: profesor?.lastname ?? 'No disponible',
        },
        {
            name: 'Correo',
            value: profesor?.email ?? 'No disponible',
        },
        {
            name: 'Usuario',
            value: profesor?.username ?? 'No disponible',
        },
        {
            name: 'Asignaturas',
            value: profesor?.subjects.map((item)=>item.name).join(', ') ?? 'No disponible',
        },
        {
            name: 'Valoracion',
            value: profesor?.valoracion?.toString() ?? 'No disponible',
        },
        {
            name: 'Salario',
            value: profesor?.salary.toString() ?? 'No disponible',
        },
        {
            name: 'Experiencia',
            value: profesor?.experience.toString() ?? 'No disponible',
        },
        {
            name: 'Tipo de contrato',
            value: profesor?.contractType ?? 'No disponible',
        },
        {
            name: 'Especialidad',
            value: profesor?.specialty ?? 'No disponible',
        },

    ]
    return (
        <div className={'size-fit mt-20'}>
            <UserCard data={userInfo}/>
        </div>
    )
}