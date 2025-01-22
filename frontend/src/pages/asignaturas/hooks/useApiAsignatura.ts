// frontend/src/pages/asignaturas/hooks/useApiAsignatura.ts
import { useContext, useState } from "react";
import { AsignaturaGetAdapter } from "../adapters/AsignaturaGetAdapter.ts";
import { AsignaturaGetDB, AsignaturaGetResponse } from "../models/AsignaturaGetDB.ts";
import { AppContext } from "../../../App.tsx";
import { EndpointType } from "../../../api/EndpointType.ts";
import apiRequest from "../../../api/apiRequest.ts";
import { AsignaturaCreateAdapter } from "../adapters/AsignaturaCreateAdapter.ts";
import { getAsignaturaCreateDbFromAdapter } from "../utils/utils.ts";

const endpoint = EndpointType.ASIGNATURAS;

export const useApiAsignatura = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [asignaturas, setAsignaturas] = useState<AsignaturaGetAdapter[]>();
    const { setError, asignaturas: asignaturasAppContext, setAsignaturas: setAsignaturasAppContext } = useContext(AppContext);

    const getAsignaturas = async () => {
        setIsLoading(true);
        if (asignaturasAppContext)
            setAsignaturas(asignaturasAppContext);
        else {
            const res = await apiRequest.getApi(endpoint);
            if (res.ok) {
                const data: AsignaturaGetResponse = await res.json();
                const asignaturaArray = Object.values(data)
                    .map((asignatura: AsignaturaGetDB) => new AsignaturaGetAdapter(asignatura));
                setAsignaturas(asignaturaArray);
                setAsignaturasAppContext!(asignaturaArray);
            } else {
                setError!(new Error(res.statusText));
            }
        }
        setIsLoading(false);
    };

    const createAsignatura = async (asignatura: AsignaturaCreateAdapter) => {
        setIsLoading(true);
        const res = await apiRequest.postApi(endpoint, getAsignaturaCreateDbFromAdapter(asignatura));
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    const updateAsignatura = async (asignatura: AsignaturaCreateAdapter) => {
        setIsLoading(true);
        const res = await apiRequest.patchApi(endpoint, getAsignaturaCreateDbFromAdapter(asignatura));
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    const deleteAsignatura = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    return {
        asignaturas,
        isLoading,
        getAsignaturas,
        createAsignatura,
        deleteAsignatura,
        updateAsignatura
    };
};