import {useState} from "react";
import {ProfesorGetAdapter} from "../adapters/ProfesorGetAdapter.ts";
import {ProfesorDB, ProfesorGetResponse} from "../models/ProfesorGetDB.ts";
import profesorApi from "../api/requests.ts";

export const useGetProfesores = (onError: (error: Error)=>void) => {
    const [isGetLoading, setIsGetLoading] = useState(false)
    const [profesores, setProfesores] = useState<ProfesorGetAdapter[]>()
    const getProfesores = async () => {
        setIsGetLoading(true)
        const res = await profesorApi.getProfesores()
        if (res.ok) {
            const data: ProfesorGetResponse = await res.json()
            setProfesores(Object.values(data)
                .map((profesor: ProfesorDB) => new ProfesorGetAdapter(profesor)))
        } else {
            onError(new Error(res.statusText))
        }
        setIsGetLoading(false)
    }

    return {
        isGetLoading,
        profesores,
        getProfesores,
    }
}