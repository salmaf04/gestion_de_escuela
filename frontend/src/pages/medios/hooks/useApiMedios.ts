import {useContext, useState} from "react";
import {MedioGetAdapter} from "../adapters/MedioGetAdapter.ts";
import {MedioGetDB, MedioGetResponse} from "../models/MedioGetDB.ts";
import {AppContext} from "../../../App.tsx";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";
import {MedioCreateAdapter} from "../adapters/MedioCreateAdapter.ts";
import {useApiAulas} from "../../aulas/hooks/useApiAulas.ts";
import {getQueryParamsFromObject} from "../../../utils/utils.ts";

const endpoint = EndpointEnum.MEDIOS

export const useApiMedio = () => {
    const [isLoading, setIsLoading] = useState(false)
    const {setError, medios: mediosAppContext, setMedios: setMediosAppContext, personalId, setMessage} = useContext(AppContext)

    const getMedios = async () => {
        setIsLoading(true)
        if (mediosAppContext) {
            setIsLoading(false)
        }
        const res = await apiRequest.getApi(endpoint)
        if (res.ok) {
            const data: MedioGetResponse = await res.json()
            const medioArray = Object.values(data)
                .map((medio: MedioGetDB) => new MedioGetAdapter(medio))
            setMediosAppContext!(medioArray)
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    const createMedio = async (medio: MedioCreateAdapter) => {
        setIsLoading(true)
        const res = await apiRequest.postApi(endpoint, medio)
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getMedios()
        setIsLoading(false)
    }
    const updateMedio = async (id: string, medio: Partial<MedioCreateAdapter>) => {
        setIsLoading(true)
        const res = await apiRequest.patchApi(endpoint, id, {}, getQueryParamsFromObject(medio))
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getMedios()
        setIsLoading(false)
    }

    const deleteMedio = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        await getMedios()
        setIsLoading(false);
    };

    const solicitarMedio = async (body: {mean_id: string}) => {
        setIsLoading(true);
        const res = await apiRequest.postApi(EndpointEnum.MEAN_REQUEST+"/"+personalId, body);
        if (!res.ok)
            setError!(new Error(res.statusText));
        else
            setMessage!("Solicitud enviada correctamente")
        await getMedios()
        setIsLoading(false);
    };
    const devolverMedio = async (mean_id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(EndpointEnum.MEAN_REQUEST, personalId!, {mean_id: mean_id});
        if (!res.ok)
            setError!(new Error(res.statusText));
        else
            setMessage!("Solicitud enviada correctamente")
        await getMedios()
        setIsLoading(false);
    };

    return {
        isLoading,
        getMedios,
        createMedio,
        deleteMedio,
        updateMedio,
        solicitarMedio,
        devolverMedio
    }
}