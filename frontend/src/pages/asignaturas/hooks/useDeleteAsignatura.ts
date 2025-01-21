import {useContext, useState} from "react";
import asignaturaApi from "../api/requests.ts";
import {AppContext} from "../../../App.tsx";

export const useDeleteAsignatura = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [deletedAsignaturaId, setDeletedAsignaturaId] = useState<string | null>(null);
    const {setError} = useContext(AppContext)

    const deleteAsignatura = async (id: string) => {
        setIsLoading(true);
        const res = await asignaturaApi.deleteAsignatura(id);
        if (res.ok) {
            setDeletedAsignaturaId(id);
        } else {
            setError!(new Error(res.statusText));
        }
        setIsLoading(false);
    };

    return {
        isLoading,
        deletedAsignaturaId,
        deleteAsignatura,
    };
};