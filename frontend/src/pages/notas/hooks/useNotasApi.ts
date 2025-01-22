// frontend/src/pages/notas/hooks/useApiNotas.ts
import { useContext, useState } from "react";
import { NotaGetAdapter } from "../adapters/NotaGetAdapter.ts";
import { NotaGetDB, NotaGetResponse } from "../models/NotaGetDB.ts";
import { AppContext } from "../../../App.tsx";
import { EndpointType } from "../../../api/EndpointType.ts";
import apiRequest from "../../../api/apiRequest.ts";
import { NotaCreateAdapter } from "../adapters/NotaCreateAdapter.ts";
import { getNotaCreateDbFromAdapter } from "../utils/utils.ts";

const endpoint = EndpointType.NOTAS;

export const useApiNotas = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [notas, setNotas] = useState<NotaGetAdapter[]>();
    const { setError, notas: notasAppContext, setNotas: setNotasAppContext } = useContext(AppContext);

    const getNotas = async () => {
        setIsLoading(true);
        if (notasAppContext)
            setNotas(notasAppContext);
        else {
            const res = await apiRequest.getApi(endpoint);
            if (res.ok) {
                const data: NotaGetResponse = await res.json();
                const notaArray = Object.values(data)
                    .map((nota: NotaGetDB) => new NotaGetAdapter(nota));
                setNotas(notaArray);
                setNotasAppContext!(notaArray);
            } else {
                setError!(new Error(res.statusText));
            }
        }
        setIsLoading(false);
    };

    const createNota = async (nota: NotaCreateAdapter) => {
        setIsLoading(true);
        const res = await apiRequest.postApi(endpoint, getNotaCreateDbFromAdapter(nota));
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    const updateNota = async (nota: NotaCreateAdapter) => {
        setIsLoading(true);
        const res = await apiRequest.patchApi(endpoint, getNotaCreateDbFromAdapter(nota));
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    const deleteNota = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    return {
        notas,
        isLoading,
        getNotas,
        createNota,
        deleteNota,
        updateNota
    };
};