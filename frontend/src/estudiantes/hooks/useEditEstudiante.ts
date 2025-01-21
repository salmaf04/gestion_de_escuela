import { useState } from "react";
import { EstudianteCreateAdapter } from "../adapters/EstudianteCreateAdapter.ts";
import { EstudianteCreateDB } from "../models/EstudianteCreateDB.ts";
import estudianteApi from "../api/requests.ts";

export const useEditEstudiante = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [editedEstudiante, setEditedEstudiante] = useState<EstudianteCreateAdapter>();

    const editEstudiante = async (estudiante: EstudianteCreateAdapter, onError: (error: Error) => void) => {
        setIsLoading(true);
        const res = await estudianteApi.putEstudiante(estudiante);
        if (res.ok) {
            const data: EstudianteCreateDB = await res.json();
            setEditedEstudiante(new EstudianteCreateAdapter(data));
        } else {
            onError(new Error(res.statusText));
        }
        setIsLoading(false);
    };

    return {
        isLoading,
        editedEstudiante,
        editEstudiante,
    };
};