// frontend/src/pages/aulas/hooks/useApiAulas.ts
import { useContext, useState } from "react";
import { AulaGetAdapter } from "../adapters/AulaGetAdapter.ts";
import { AulaGetDB, AulaGetResponse } from "../models/AulaGetDB.ts";
import { AppContext } from "../../../App.tsx";
import { EndpointType } from "../../../api/EndpointType.ts";
import apiRequest from "../../../api/apiRequest.ts";
import { AulaCreateAdapter } from "../adapters/AulaCreateAdapter.ts";
import { getAulaCreateDbFromAdapter } from "../utils/utils.ts";

const endpoint = EndpointType.AULAS;

export const useApiAulas = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [aulas, setAulas] = useState<AulaGetAdapter[]>();
    const { setError, aulas: aulasAppContext, setAulas: setAulasAppContext } = useContext(AppContext);

    const getAulas = async () => {
        setIsLoading(true);
        if (aulasAppContext)
            setAulas(aulasAppContext);
        else {
            const res = await apiRequest.getApi(endpoint);
            if (res.ok) {
                const data: AulaGetResponse = await res.json();
                const aulaArray = Object.values(data)
                    .map((aula: AulaGetDB) => new AulaGetAdapter(aula));
                setAulas(aulaArray);
                setAulasAppContext!(aulaArray);
            } else {
                setError!(new Error(res.statusText));
            }
        }
        setIsLoading(false);
    };

    const createAula = async (aula: AulaCreateAdapter) => {
        setIsLoading(true);
        const res = await apiRequest.postApi(endpoint, getAulaCreateDbFromAdapter(aula));
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    const updateAula = async (aula: AulaCreateAdapter) => {
        setIsLoading(true);
        const res = await apiRequest.patchApi(endpoint, getAulaCreateDbFromAdapter(aula));
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    const deleteAula = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    return {
        aulas,
        isLoading,
        getAulas,
        createAula,
        deleteAula,
        updateAula
    };
};