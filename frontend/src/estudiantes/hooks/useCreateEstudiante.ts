import {useContext, useState} from "react";
import {EstudianteCreateAdapter} from "../adapters/EstudianteCreateAdapter.ts";
import {EstudianteCreateDto} from "../models/EstudianteCreateDto.ts";
import estudianteApi from "../api/requests.ts";
import {AppContext} from "../../App.tsx";

export const useCreateEstudiante = () => {
    const [isLoading, setIsLoading] = useState(false)
    const [newEstudiante, setNewEstudiante] = useState<EstudianteCreateAdapter>()
    const {setError} = useContext(AppContext)

    const createEstudiante = async (estudiante: EstudianteCreateAdapter) => {

        setIsLoading(true)
        const res = await estudianteApi.postEstudiante(estudiante)
        if (res.ok) {
            const data: EstudianteCreateDto = await res.json()
            setNewEstudiante(new EstudianteCreateAdapter(data))
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    return {
        isLoading,
        newEstudiante,
        createEstudiante,
    }
}