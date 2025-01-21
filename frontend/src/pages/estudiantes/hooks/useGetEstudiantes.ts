import { useState } from "react";
import { EstudianteGetAdapter } from "../adapters/EstudianteGetAdapter.ts";
import { EstudianteGetDB, EstudianteGetResponse } from "../models/EstudianteGetDB.ts";
import estudianteApi from "../api/requests.ts";


export const useGetEstudiantes = (onError: (error: Error) => void) => {
    const [isGetLoading, setIsGetLoading] = useState(false);
    const [estudiantes, setEstudiantes] = useState<EstudianteGetAdapter[]>();
    const isMocked = false;

    const getEstudiantes = async () => {
        setIsGetLoading(true);
        if (isMocked) {

        } else {
            const res = await estudianteApi.getEstudiantes();
            if (res.ok) {
                const data: EstudianteGetResponse = await res.json();
                setEstudiantes(Object.values(data).map((estudiante: EstudianteGetDB) => new EstudianteGetAdapter(estudiante)));
            } else {
                onError(new Error(res.statusText));
            }
        }
        setIsGetLoading(false);
    };

    return {
        isGetLoading,
        estudiantes,
        getEstudiantes,
    };
};