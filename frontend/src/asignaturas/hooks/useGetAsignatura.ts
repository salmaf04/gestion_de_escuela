import {useContext, useState} from "react";
import {AsignaturaDB, AsignaturaGetDB} from "../models/AsignaturaGetDB.ts";
import asignaturaApi from "../api/requests.ts";
import {AppContext} from "../../App.tsx";
import {AsignaturaGetAdapter} from "../adapters/AsignaturaGetAdapter.ts";

export const useGetAsignaturas = () => {
    const [isGetLoading, setIsGetLoading] = useState(false)
    const [asignaturas, setAsignaturas] = useState<AsignaturaGetDB[]>()
    const {setError} = useContext(AppContext)


    const getAsignaturas = async () => {
        setIsGetLoading(true)
        const res = await asignaturaApi.getAsignaturas()
        if (res.ok) {
            const data: AsignaturaGetDB = await res.json()

            setAsignaturas(Object.values(data)
                .map((asignatura: AsignaturaDB) => new AsignaturaGetAdapter(asignatura)))
        } else {
            setError!(new Error(res.statusText))
        }
        setIsGetLoading(false)
    }

    return {
        isGetLoading,
        asignaturas,
        getAsignaturas,
    }
}