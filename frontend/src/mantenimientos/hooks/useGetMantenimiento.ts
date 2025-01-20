import {useContext, useState} from "react";
import mantenimientoApi from "../api/requests.ts";
import {AppContext} from "../../App.tsx";
import {MantenimientoGetAdapter} from "../adapters/MantenimientoGetAdapter.ts";
import {MantenimientoDB, MantenimientoGetResponse} from "../models/MantenimientoGetResponse.ts";

export const useGetMantenimientos = () => {
    const [isGetLoading, setIsGetLoading] = useState(false)
    const [mantenimientos, setMantenimientos] = useState<MantenimientoGetResponse[]>()
    const {setError} = useContext(AppContext)


    const getMantenimientos = async () => {
        setIsGetLoading(true)
        const res = await mantenimientoApi.getMantenimientos()
        if (res.ok) {
            const data: MantenimientoGetResponse = await res.json()

            setMantenimientos(Object.values(data)
                .map((mantenimiento: MantenimientoDB) => new MantenimientoGetAdapter(mantenimiento)))
        } else {
            setError!(new Error(res.statusText))
        }
        setIsGetLoading(false)
    }

    return {
        isGetLoading,
        mantenimientos,
        getMantenimientos,
    }
}