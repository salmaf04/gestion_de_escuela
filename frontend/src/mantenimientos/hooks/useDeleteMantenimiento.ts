import {useContext, useState} from "react";
import mantenimientoApi from "../api/requests.ts";
import {AppContext} from "../../App.tsx";

export const useDeleteMantenimiento = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [deletedMantenimientoId, setDeletedMantenimientoId] = useState<string | null>(null);
    const {setError} = useContext(AppContext)

    const deleteMantenimiento = async (id: string) => {
        setIsLoading(true);
        const res = await mantenimientoApi.deleteMantenimiento(id);
        if (res.ok) {
            setDeletedMantenimientoId(id);
        } else {
            setError!(new Error(res.statusText));
        }
        setIsLoading(false);
    };

    return {
        isLoading,
        deletedMantenimientoId,
        deleteMantenimiento,
    };
};