import {useContext, useState} from "react";
import aularApi from "../api/requests.ts";
import {AppContext} from "../../../App.tsx";
import {AulaCreateAdapter} from "../adapters/AulaCreateAdapter.ts";
import {AulaCreateDB} from "../models/AulaCreateDB.ts";

export const useEditAula = () => {
    const [isLoading, setIsLoading] = useState(false)
    const [editedAula, setEditedAula] = useState<AulaCreateAdapter>()
    const {setError} = useContext(AppContext)

    const editAula = async (aula: AulaCreateAdapter) => {
        setIsLoading(true)
        const res = await aularApi.putAula(aula)
        if (res.ok) {
            const data: AulaCreateDB = await res.json()
            setEditedAula(new AulaCreateAdapter(data))
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    return {
        isLoading,
        editedAula,
        editAula,
    }
}