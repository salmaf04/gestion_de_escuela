import {useContext, useState} from "react";
import {ProfesorGetAdapter} from "../adapters/ProfesorGetAdapter.ts";
import {ProfesorDB, ProfesorGetResponse} from "../models/ProfesorGetDB.ts";
import profesorApi from "../api/requests.ts";
import {dataExample} from "../data/Example_data.tsx";
import {AppContext} from "../../App.tsx";

export const useGetProfesores = () => {
    const [isGetLoading, setIsGetLoading] = useState(false)
    const [profesores, setProfesores] = useState<ProfesorGetAdapter[]>()
    const {setError} = useContext(AppContext)

    const isMocked = false;

    const getProfesores = async () => {
        setIsGetLoading(true)
        if (isMocked) {
            setTimeout(() => {
                setProfesores(dataExample.map((profesor: ProfesorDB) => new ProfesorGetAdapter(profesor)))
            }, 3000)
        }
        else {
            const res = await profesorApi.getProfesores()
            if (res.ok) {
                const data: ProfesorGetResponse = await res.json()

                setProfesores(Object.values(data)
                    .map((profesor: ProfesorDB) => new ProfesorGetAdapter(profesor)))
            } else {
                setError!(new Error(res.statusText))
            }
        }
        setIsGetLoading(false)
    }

    return {
        isGetLoading,
        profesores,
        getProfesores,
    }
}