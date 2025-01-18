import { useState } from "react";
import profesorApi from "../api/requests.ts";

export const useDeleteProfesor = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [deletedProfesorId, setDeletedProfesorId] = useState<string | null>(null);

    const deleteProfesor = async (id: string, onError: (error: Error) => void) => {
        setIsLoading(true);
        const res = await profesorApi.deleteProfesor(id);
        if (res.ok) {
            setDeletedProfesorId(id);
        } else {
            onError(new Error(res.statusText));
        }
        setIsLoading(false);
    };

    return {
        isLoading,
        deletedProfesorId,
        deleteProfesor,
    };
};