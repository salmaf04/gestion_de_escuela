import {useContext, useState} from "react";
import {ProfesorCreateAdapter} from "../adapters/ProfesorCreateAdapter.ts";
import {ProfesorCreateDB} from "../models/ProfesorCreateDB.ts";
import profesorApi from "../api/requests.ts";
import {AppContext} from "../../App.tsx";

export const useCreateProfesor = () => {
    const [isLoading, setIsLoading] = useState(false)
    const [newProfesor, setNewProfesor] = useState<ProfesorCreateAdapter>()
    const {setError} = useContext(AppContext)

    const createProfesor = async (profesor: ProfesorCreateAdapter) => {

        setIsLoading(true)
        const res = await profesorApi.postProfesor(profesor)
        if (res.ok) {
            const data: ProfesorCreateDB = await res.json()
            setNewProfesor(new ProfesorCreateAdapter(data))
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    return {
        isLoading,
        newProfesor,
        createProfesor,
    }
}