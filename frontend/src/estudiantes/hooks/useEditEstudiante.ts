import {useContext, useState} from "react";
import {EstudianteCreateAdapter} from "../adapters/EstudianteCreateAdapter.ts";
import {EstudianteCreateDto} from "../models/EstudianteCreateDto.ts";
import estudianterApi from "../api/requests.ts";
import {AppContext} from "../../App.tsx";

export const useEditEstudiante = () => {
    const [isLoading, setIsLoading] = useState(false)
    const [editedEstudiante, setEditedEstudiante] = useState<EstudianteCreateAdapter>()
    const {setError} = useContext(AppContext)

    const editEstudiante = async (estudiante: EstudianteCreateAdapter) => {
        setIsLoading(true)
        const res = await estudianterApi.putEstudiante(estudiante)
        if (res.ok) {
            const data: EstudianteCreateDto = await res.json()
            setEditedEstudiante(new EstudianteCreateAdapter(data))
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    return {
        isLoading,
        editedEstudiante,
        editEstudiante,
    }
}