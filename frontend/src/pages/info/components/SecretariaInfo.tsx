import {useContext, useEffect} from "react";
import {AppContext} from "../../../App.tsx";
import {useApiSecretarias} from "../hooks/useApiSecretaria.ts";

export default function SecretariaInfo(){
    const {getSecretaria, secretaria} = useApiSecretarias()
    const {personalId} = useContext(AppContext)
    useEffect(() => {
        getSecretaria(personalId!)
    }, []);
    return(
        <>
            <div className={''}>

            </div>
            <span>Nombre: {secretaria?.name}</span>
            <span>Apellidos: {secretaria?.lastname}</span>
            <span>Correo: {secretaria?.email}</span>
            <span>Usuario:{secretaria?.username}</span>
        </>
    )
}