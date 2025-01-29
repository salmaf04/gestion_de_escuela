import {useApiProfesor} from "../../profesores/hooks/useApiProfesor.ts";
import {useContext, useEffect} from "react";
import {AppContext} from "../../../App.tsx";

export default function ProfesorInfo(){
    const {getProfesor, profesor} = useApiProfesor()
    const {personalId} = useContext(AppContext)
    useEffect(() => {
        getProfesor(personalId!)
    }, []);
    return(
        <>
            <div className={''}>

            </div>
            <span>Nombre: {profesor?.name}</span>
            <span>Apellidos: {profesor?.lastname}</span>
            <span>Especialidad: {profesor?.specialty}</span>
            <span>Especialidad: {profesor?.contractType}</span>
            <span>Experiencia: {profesor?.experience}</span>
            <span>Salario: {profesor?.salary}</span>
            <span>Correo: {profesor?.email}</span>
            <span>Usuario:{profesor?.username}</span>
            <span>Asignaturas: {profesor?.specialty}</span>
            <span>Valoracion: {profesor?.valoracion}</span>
        </>
    )
}