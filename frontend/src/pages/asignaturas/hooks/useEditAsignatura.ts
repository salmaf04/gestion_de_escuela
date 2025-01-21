import {useContext, useState} from "react";
import {AsignaturaCreateAdapter} from "../adapters/AsignaturaCreateAdapter.ts";
import {AsignaturaCreateDto} from "../models/AsignaturaCreateDB.ts";
import asignaturarApi from "../api/requests.ts";
import {AppContext} from "../../../App.tsx";

export const useEditAsignatura = () => {
    const [isLoading, setIsLoading] = useState(false)
    const [editedAsignatura, setEditedAsignatura] = useState<AsignaturaCreateAdapter>()
    const {setError} = useContext(AppContext)

    const editAsignatura = async (asignatura: AsignaturaCreateAdapter) => {
        setIsLoading(true)
        const res = await asignaturarApi.putAsignatura(asignatura)
        if (res.ok) {
            const data: AsignaturaCreateDto = await res.json()
            setEditedAsignatura(new AsignaturaCreateAdapter(data))
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    return {
        isLoading,
        editedAsignatura,
        editAsignatura,
    }
}