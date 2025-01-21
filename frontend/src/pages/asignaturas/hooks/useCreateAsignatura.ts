import {useContext, useState} from "react";
import {AsignaturaCreateAdapter} from "../adapters/AsignaturaCreateAdapter.ts";
import {AsignaturaCreateDto} from "../models/AsignaturaCreateDB.ts";
import asignaturaApi from "../api/requests.ts";
import {AppContext} from "../../../App.tsx";

export const useCreateAsignatura = () => {
    const [isLoading, setIsLoading] = useState(false)
    const [newAsignatura, setNewAsignatura] = useState<AsignaturaCreateAdapter>()
    const {setError} = useContext(AppContext)

    const createAsignatura = async (asignatura: AsignaturaCreateAdapter) => {

        setIsLoading(true)
        const res = await asignaturaApi.postAsignatura(asignatura)
        if (res.ok) {
            const data: AsignaturaCreateDto = await res.json()
            setNewAsignatura(new AsignaturaCreateAdapter(data))
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    return {
        isLoading,
        newAsignatura,
        createAsignatura,
    }
}