import {useContext, useState} from "react";
import {EstudianteDB, EstudianteGetResponse} from "../models/EstudianteGetResponse.ts";
import estudianteApi from "../api/requests.ts";
import {AppContext} from "../../App.tsx";
import {EstudianteGetAdapter} from "../adapters/EstudianteGetAdapter.ts";

export const useGetEstudiantes = () => {
    const [isGetLoading, setIsGetLoading] = useState(false)
    const [estudiantes, setEstudiantes] = useState<EstudianteGetResponse[]>()
    const {setError} = useContext(AppContext)


    const getEstudiantes = async () => {
        setIsGetLoading(true)
        const res = await estudianteApi.getEstudiantes()
        if (res.ok) {
            const data: EstudianteGetResponse = await res.json()

            setEstudiantes(Object.values(data)
                .map((estudiante: EstudianteDB) => new EstudianteGetAdapter(estudiante)))
        } else {
            setError!(new Error(res.statusText))
        }
        setIsGetLoading(false)
    }

    return {
        isGetLoading,
        estudiantes,
        getEstudiantes,
    }
}