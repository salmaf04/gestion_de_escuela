import {useState} from "react";
import {ProfesorGetAdapter} from "../adapters/ProfesorGetAdapter.ts";
import {ProfesorDB, ProfesorGetResponse} from "../models/ProfesorGetDB.ts";
import profesorApi from "./requests.ts";

export const useGetProfesores = () => {
    const [isGetLoading, setIsGetLoading] = useState(false)
    const [profesores, setProfesores] = useState<ProfesorGetAdapter[]>()
    const [getError, setGetError] = useState<Error>()
    const getProfesores = async () => {
        setIsGetLoading(true)
        const res = await profesorApi.getProfesores()
        if (res.ok) {
            const data: ProfesorGetResponse = await res.json()
            setProfesores(Object.values(data)
                .map((profesor: ProfesorDB) => new ProfesorGetAdapter(profesor)))
        } else {
            setGetError(new Error(res.statusText))
        }
        setIsGetLoading(false)
    }

    return {
        isGetLoading,
        profesores,
        getProfesores,
        getError
    }
}