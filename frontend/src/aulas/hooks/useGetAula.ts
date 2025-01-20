import {useContext, useState} from "react";
import aulaApi from "../api/requests.ts";
import {AppContext} from "../../App.tsx";
import {AulaDB, AulaGetResponse} from "../models/AulaGetResponse.ts";
import {AulaGetAdapter} from "../adapters/AulaGetAdapter.ts";

export const useGetAulas = () => {
    const [isGetLoading, setIsGetLoading] = useState(false)
    const [aulas, setAulas] = useState<AulaGetResponse[]>()
    const {setError} = useContext(AppContext)


    const getAulas = async () => {
        setIsGetLoading(true)
        const res = await aulaApi.getAulas()
        if (res.ok) {
            const data: AulaGetResponse = await res.json()

            setAulas(Object.values(data)
                .map((aula: AulaDB) => new AulaGetAdapter(aula)))
        } else {
            setError!(new Error(res.statusText))
        }
        setIsGetLoading(false)
    }

    return {
        isGetLoading,
        aulas,
        getAulas,
    }
}