import {useContext, useState} from "react";
import estudianteApi from "../api/requests.ts";
import {AppContext} from "../../App.tsx";

export const useDeleteEstudiante = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [deletedEstudianteId, setDeletedEstudianteId] = useState<string | null>(null);
    const {setError} = useContext(AppContext)

    const deleteEstudiante = async (id: string) => {
        setIsLoading(true);
        const res = await estudianteApi.deleteEstudiante(id);
        if (res.ok) {
            setDeletedEstudianteId(id);
        } else {
            setError!(new Error(res.statusText));
        }
        setIsLoading(false);
    };

    return {
        isLoading,
        deletedEstudianteId,
        deleteEstudiante,
    };
};