import {useState} from "react";
import {ProfesorCreateAdapter} from "../adapters/ProfesorCreateAdapter.ts";
import {ProfesorCreateDB} from "../models/ProfesorCreateDB.ts";
import profesorApi from "./requests.ts";

export const useCreateProfesor = () => {
    const [isLoading, setIsLoading] = useState(false)
    const [newProfesor, setNewProfesor] = useState<ProfesorCreateAdapter>()
    const [createError, setGetError] = useState<Error>()

    const createProfesor = async (profesor: ProfesorCreateAdapter) => {
        setIsLoading(true)
        const res = await profesorApi.postProfesor(profesor)
        if (res.ok) {
            const data: ProfesorCreateDB = await res.json()
            setNewProfesor(new ProfesorCreateAdapter(data))
        } else {
            setGetError(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    return {
        isLoading,
        newProfesor,
        createProfesor,
        createError
    }
}