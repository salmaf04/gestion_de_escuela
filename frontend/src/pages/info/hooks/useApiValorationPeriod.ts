// frontend/src/pages/secretarias/hooks/useApiAusencias.ts
import { useContext, useState } from "react";
import { AppContext } from "../../../App.tsx";
import apiRequest from "../../../api/apiRequest.ts";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import { IValorationPeriod } from "../models/IValorationPeriod.ts";

const endpoint = EndpointEnum.VALORATION_PERIOD;

export const useApiValorationPeriod = () => {
    const [isLoading, setIsLoading] = useState(false);
    const {valorationPeriod, setvalorationPeriod, setError} = useContext(AppContext)
    const getValorationPeriod = async () => {
        setIsLoading(true);
        if (valorationPeriod)
            setvalorationPeriod!(valorationPeriod);

        const res = await apiRequest.getApi(endpoint);
        if (res.ok){
            const data: IValorationPeriod = await res.json()
            setvalorationPeriod!(data)
        }
        else
            setError!(new Error(res.statusText));
        setIsLoading(false);
    };

    const updateValorationPeriod = async (valoration_period: boolean) => {
        setIsLoading(true)
        const res = await apiRequest.patchApi(endpoint, "", {open: valoration_period})
        if (!res.ok)
            setError!(new Error(res.statusText))
        getValorationPeriod()
        setIsLoading(false)
    }

    return {
        isLoading,
        getValorationPeriod,
        updateValorationPeriod,
        valorationPeriod
    };
};