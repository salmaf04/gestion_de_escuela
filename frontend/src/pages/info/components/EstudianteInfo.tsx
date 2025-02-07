import {useContext, useEffect} from "react";
import {AppContext} from "../../../App.tsx";
import UserCard, {UserDataProp} from "./UserCard.tsx";
import {useApiEstudiante} from "../../estudiantes/hooks/useApiEstudiante.ts";

export default function EstudianteInfo() {
    const {getEstudiante, estudiante} = useApiEstudiante()
    const {personalId} = useContext(AppContext)
    useEffect(() => {
        getEstudiante(personalId!)
    }, []);
    const userInfo: UserDataProp[] = [
        {
            name: 'Nombre',
            value: estudiante?.name ?? 'No disponible',
        },
        {
            name: 'Apellidos',
            value: estudiante?.lastname ?? 'No disponible',
        },
        {
            name: 'Edad',
            value: estudiante?.age.toString() ?? 'No disponible'
        },
        {
            name: 'Actividades Extra',
            value: estudiante?.extra_activities ? 'Sí' : 'No',
        },
        {
            name: 'Curso',
            value: estudiante?.course.year.toString() ?? 'No disponible',
        },
        {
            name: 'Correo',
            value: estudiante?.email ?? 'No disponible',
        },
        {
            name: 'Usuario',
            value: estudiante?.username ?? 'No disponible',
        },
    ]
    return (
        <div className={'size-fit mt-20'}>
            <UserCard data={userInfo}/>
        </div>
    )
}