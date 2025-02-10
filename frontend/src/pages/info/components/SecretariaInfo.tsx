import {useContext, useEffect, useState} from "react";
import {AppContext} from "../../../App.tsx";
import {useApiSecretaria} from "../hooks/useApiSecretaria.ts";
import UserCard, {UserDataProp} from "./UserCard.tsx";
import Toggle from "../../../components/Toggle.tsx";
import {useApiValorationPeriod} from "../hooks/useApiValorationPeriod.ts";

export default function SecretariaInfo(){
    const {getSecretaria, secretaria} = useApiSecretaria()
    const {personalId,valorationPeriod} = useContext(AppContext)
    const {updateValorationPeriod} = useApiValorationPeriod()
    const [isValorationPeriod, setIsValorationPeriod] = useState(valorationPeriod?.open ?? false)
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
        <div className={'size-fit mt-20 flex w-full justify-between'}>
            <div className={'w-full'}>
                <UserCard data={userInfo}/>
            </div>
            <div className={'w-full'}>
                <h1 className={'text-indigo-600 font-bold text-xl'}>Configuraciones: </h1>
                <div className={'mt-10'}>
                    <div className={'flex space-x-5'}>
                        <p className={'text-slate-500 font-semibold'}>Período de valoraciones: </p>
                        <Toggle enabled={valorationPeriod?.open ?? false} setEnabled={updateValorationPeriod}/>
                    </div>
                </div>
            </div>

        </div>
    )
}