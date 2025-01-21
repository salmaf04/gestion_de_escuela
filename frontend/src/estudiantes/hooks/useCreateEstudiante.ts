import { useState } from "react";
import { EstudianteCreateAdapter } from "../adapters/EstudianteCreateAdapter.ts";
import { EstudianteCreateDB } from "../models/EstudianteCreateDB.ts";
import estudianteApi from "../api/requests.ts";

export const useCreateEstudiante = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [newEstudiante, setNewEstudiante] = useState<EstudianteCreateAdapter>();

    const createEstudiante = async (estudiante: EstudianteCreateAdapter, onError: (error: Error) => void) => {
        setIsLoading(true);
        const res = await estudianteApi.postEstudiante(estudiante);
        if (res.ok) {
            const data: EstudianteCreateDB = await res.json();
            setNewEstudiante(new EstudianteCreateAdapter(data));
        } else {
            onError(new Error(res.statusText));
        }
        setIsLoading(false);
    };

    return {
        isLoading,
        newEstudiante,
        createEstudiante,
    };
};