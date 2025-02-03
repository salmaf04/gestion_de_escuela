import {useContext, useEffect} from "react";
import {AppContext} from "../../../App.tsx";
import {useApiAdministradores} from "../hooks/useApiAdministrador.ts";

export default function AdministradorInfo(){
    const {getAdministrador, administrador} = useApiAdministradores()
    const {personalId} = useContext(AppContext)
    useEffect(() => {
        getAdministrador(personalId!)
    }, []);
    return(
        <>
            <div className={''}>

            </div>
            <span>Nombre: {administrador?.name}</span>
            <span>Apellidos: {administrador?.lastname}</span>
            <span>Correo: {administrador?.email}</span>
            <span>Usuario:{administrador?.username}</span>
        </>
    )
}