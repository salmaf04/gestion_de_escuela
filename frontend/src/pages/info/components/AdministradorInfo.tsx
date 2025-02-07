import {useContext, useEffect} from "react";
import {AppContext} from "../../../App.tsx";
import UserCard, {UserDataProp} from "./UserCard.tsx";
import {useApiAdministrador} from "../hooks/useApiAdministrador.ts";

export default function AdministradorInfo(){
    const {getAdministrador, administrador} = useApiAdministrador()
    const {personalId} = useContext(AppContext)
    useEffect(() => {
        getAdministrador(personalId!)
    }, []);
    const userInfo: UserDataProp[] = [
        {
            name: 'Nombre',
            value: administrador?.name ?? 'No disponible',
        },
        {
            name: 'Apellidos',
            value: administrador?.lastname ?? 'No disponible',
        },
        {
            name: 'Correo',
            value: administrador?.email ?? 'No disponible',
        },
        {
            name: 'Usuario',
            value: administrador?.username ?? 'No disponible',
        }
    ]
    return(
        <div className={'size-fit mt-20'}>
            <UserCard data={userInfo}/>
        </div>
    )
}