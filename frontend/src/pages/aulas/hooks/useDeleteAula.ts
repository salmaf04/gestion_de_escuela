import {useContext, useState} from "react";
import aulaApi from "../api/requests.ts";
import {AppContext} from "../../../App.tsx";

export const useDeleteAula = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [deletedAulaId, setDeletedAulaId] = useState<string | null>(null);
    const {setError} = useContext(AppContext)

    const deleteAula = async (id: string) => {
        setIsLoading(true);
        const res = await aulaApi.deleteAula(id);
        if (res.ok) {
            setDeletedAulaId(id);
        } else {
            setError!(new Error(res.statusText));
        }
        setIsLoading(false);
    };

    return {
        isLoading,
        deletedAulaId,
        deleteAula,
    };
};