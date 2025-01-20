import {useContext, useState} from "react";
import medioApi from "../api/requests.ts";
import {AppContext} from "../../App.tsx";

export const useDeleteMedio = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [deletedMedioId, setDeletedMedioId] = useState<string | null>(null);
    const {setError} = useContext(AppContext)

    const deleteMedio = async (id: string) => {
        setIsLoading(true);
        const res = await medioApi.deleteMedio(id);
        if (res.ok) {
            setDeletedMedioId(id);
        } else {
            setError!(new Error(res.statusText));
        }
        setIsLoading(false);
    };

    return {
        isLoading,
        deletedMedioId,
        deleteMedio,
    };
};