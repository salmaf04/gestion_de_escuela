import {useContext, useState} from "react";
import mantenimientorApi from "../api/requests.ts";
import {AppContext} from "../../../App.tsx";
import {MantenimientoCreateAdapter} from "../adapters/MantenimientoCreateAdapter.ts";
import {MantenimientoCreateDto} from "../models/MantenimientoCreateDto.ts";

export const useEditMantenimiento = () => {
    const [isLoading, setIsLoading] = useState(false)
    const [editedMantenimiento, setEditedMantenimiento] = useState<MantenimientoCreateAdapter>()
    const {setError} = useContext(AppContext)

    const editMantenimiento = async (mantenimiento: MantenimientoCreateAdapter) => {
        setIsLoading(true)
        const res = await mantenimientorApi.putMantenimiento(mantenimiento)
        if (res.ok) {
            const data: MantenimientoCreateDto = await res.json()
            setEditedMantenimiento(new MantenimientoCreateAdapter(data))
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    return {
        isLoading,
        editedMantenimiento,
        editMantenimiento,
    }
}