import {useContext, useEffect} from "react";
import {AppContext} from "../../../App.tsx";
import {useApiSecretaria} from "../hooks/useApiSecretaria.ts";
import UserCard, {UserDataProp} from "./UserCard.tsx";

export default function SecretariaInfo(){
    const {getSecretaria, secretaria} = useApiSecretaria()
    const {personalId} = useContext(AppContext)
    useEffect(() => {
        getSecretaria(personalId!)
    }, []);
    const userInfo: UserDataProp[] = [
        {
            name: 'Nombre',
            value: secretaria?.name ?? 'No disponible',
        },
        {
            name: 'Apellidos',
            value: secretaria?.lastname ?? 'No disponible',
        },
        {
            name: 'Correo',
            value: secretaria?.email ?? 'No disponible',
        },
        {
            name: 'Usuario',
            value: secretaria?.username ?? 'No disponible',
        }
    ]
    return(
        <div className={'size-fit mt-20'}>
            <UserCard data={userInfo}/>
        </div>
    )
}