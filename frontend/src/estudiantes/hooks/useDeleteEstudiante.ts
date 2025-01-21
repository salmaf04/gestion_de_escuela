import { useState } from "react";
import estudianteApi from "../api/requests.ts";

export const useDeleteEstudiante = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [deletedEstudianteId, setDeletedEstudianteId] = useState<string | null>(null);

    const deleteEstudiante = async (id: string, onError: (error: Error) => void) => {
        setIsLoading(true);
        const res = await estudianteApi.deleteEstudiante(id);
        if (res.ok) {
            setDeletedEstudianteId(id);
        } else {
            onError(new Error(res.statusText));
        }
        setIsLoading(false);
    };

    return {
        isLoading,
        deletedEstudianteId,
        deleteEstudiante,
    };
};