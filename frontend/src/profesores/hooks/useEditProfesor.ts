import {useContext, useState} from "react";
import {ProfesorCreateAdapter} from "../adapters/ProfesorCreateAdapter.ts";
import {ProfesorCreateDB} from "../models/ProfesorCreateDB.ts";
import profesorApi from "../api/requests.ts";
import {AppContext} from "../../App.tsx";

export const useEditProfesor = () => {
    const [isLoading, setIsLoading] = useState(false)
    const [editedProfesor, setEditedProfesor] = useState<ProfesorCreateAdapter>()
    const {setError} = useContext(AppContext)

    const editProfesor = async (profesor: ProfesorCreateAdapter) => {
        setIsLoading(true)
        const res = await profesorApi.putProfesor(profesor)
        if (res.ok) {
            const data: ProfesorCreateDB = await res.json()
            setEditedProfesor(new ProfesorCreateAdapter(data))
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    return {
        isLoading,
        editedProfesor,
        editProfesor,
    }
}