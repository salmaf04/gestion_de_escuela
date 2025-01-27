// frontend/src/pages/medios/hooks/useApiMedios.ts
import { useContext, useState } from "react";
import { MedioGetAdapter } from "../adapters/MedioGetAdapter.ts";
import { MedioGetDB, MedioGetResponse } from "../models/MedioGetDB.ts";
import { AppContext } from "../../../App.tsx";
import { EndpointEnum } from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";
import { MedioCreateAdapter } from "../adapters/MedioCreateAdapter.ts";
import { getMedioCreateDbFromAdapter } from "../utils/utils.ts";

const endpoint = EndpointEnum.MEDIOS;

export const useApiMedios = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [medios, setMedios] = useState<MedioGetAdapter[]>();
    const { setError, medios: mediosAppContext, setMedios: setMediosAppContext } = useContext(AppContext);

    const getMedios = async () => {
        setIsLoading(true);
        if (mediosAppContext)
            setMedios(mediosAppContext);
        else {
            const res = await apiRequest.getApi(endpoint);
            if (res.ok) {
                const data: MedioGetResponse = await res.json();
                const medioArray = Object.values(data)
                    .map((medio: MedioGetDB) => new MedioGetAdapter(medio));
                setMedios(medioArray);
                setMediosAppContext!(medioArray);
            } else {
                setError!(new Error(res.statusText));
            }
        }
        setIsLoading(false);
    };

    const createMedio = async (medio: MedioCreateAdapter) => {
        setIsLoading(true);
        const res = await apiRequest.postApi(endpoint, getMedioCreateDbFromAdapter(medio));
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    const updateMedio = async (medio: MedioCreateAdapter) => {
        setIsLoading(true);
        const res = await apiRequest.patchApi(endpoint, getMedioCreateDbFromAdapter(medio));
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    const deleteMedio = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    return {
        medios,
        isLoading,
        getMedios,
        createMedio,
        deleteMedio,
        updateMedio
    };
};