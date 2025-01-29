import {useContext, useEffect} from "react";
import {AppContext} from "../../../App.tsx";
import {useApiEstudiante} from "../../estudiantes/hooks/useApiEstudiante.ts";

export default function EstudianteInfo(){
    const {getEstudiante, estudiante} = useApiEstudiante()
    const {personalId} = useContext(AppContext)
    useEffect(() => {
        getEstudiante(personalId!)
    }, []);
    return(
        <>
            <span>Nombre: {estudiante?.name}</span>
            <span>Edad: {estudiante?.age}</span>
            <span>Correo: {estudiante?.email}</span>
            <span>Usuario:{estudiante?.username}</span>
            <span>Actividades Extra: {estudiante?.extra_activities}</span>
            <span>Curso: {estudiante?.course.year}</span>
        </>
    )
}