import {useContext, useState} from "react";
import profesorApi from "../api/requests.ts";
import {AppContext} from "../../App.tsx";

export const useDeleteProfesor = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [deletedProfesorId, setDeletedProfesorId] = useState<string | null>(null);
    const {setError} = useContext(AppContext)

    const deleteProfesor = async (id: string) => {
        setIsLoading(true);
        const res = await profesorApi.deleteProfesor(id);
        if (res.ok) {
            setDeletedProfesorId(id);
        } else {
            setError!(new Error(res.statusText));
        }
        setIsLoading(false);
    };

    return {
        isLoading,
        deletedProfesorId,
        deleteProfesor,
    };
};