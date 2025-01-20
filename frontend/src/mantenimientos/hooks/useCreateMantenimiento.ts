import {useContext, useState} from "react";
import mantenimientoApi from "../api/requests.ts";
import {AppContext} from "../../App.tsx";
import {MantenimientoCreateAdapter} from "../adapters/MantenimientoCreateAdapter.ts";
import {MantenimientoCreateDto} from "../models/MantenimientoCreateDto.ts";

export const useCreateMantenimiento = () => {
    const [isLoading, setIsLoading] = useState(false)
    const [newMantenimiento, setNewMantenimiento] = useState<MantenimientoCreateAdapter>()
    const {setError} = useContext(AppContext)

    const createMantenimiento = async (mantenimiento: MantenimientoCreateAdapter) => {

        setIsLoading(true)
        const res = await mantenimientoApi.postMantenimiento(mantenimiento)
        if (res.ok) {
            const data: MantenimientoCreateDto = await res.json()
            setNewMantenimiento(new MantenimientoCreateAdapter(data))
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    return {
        isLoading,
        newMantenimiento,
        createMantenimiento,
    }
}