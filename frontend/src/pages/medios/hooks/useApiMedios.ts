import {useContext, useState} from "react";
import {MedioGetAdapter} from "../adapters/MedioGetAdapter.ts";
import {MedioGetDB, MedioGetResponse} from "../models/MedioGetDB.ts";
import {AppContext} from "../../../App.tsx";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";
import {MedioCreateAdapter} from "../adapters/MedioCreateAdapter.ts";
import {useApiAulas} from "../../aulas/hooks/useApiAulas.ts";

const endpoint = EndpointEnum.MEDIOS

export const useApiMedio = () => {
    const [isLoading, setIsLoading] = useState(false)
    const {setError, medios: mediosAppContext, setMedios: setMediosAppContext, aulas} = useContext(AppContext)
    const {getAulas} = useApiAulas()

    const getMedios = async () => {
        setIsLoading(true)
        if (mediosAppContext) {
            setIsLoading(false)
        }
        const res = await apiRequest.getApi(endpoint)
        await getAulas()
        if (res.ok) {
            const data: MedioGetResponse = await res.json()
            const medioArray = Object.values(data)
                .map((medio: MedioGetDB) => new MedioGetAdapter(
                    medio,
                    aulas!.find((item) => item.id === medio.classroom_id)!))
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
        const res = await apiRequest.patchApi(endpoint, id, medio)
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

    return {
        isLoading,
        getMedios,
        createMedio,
        deleteMedio,
        updateMedio
    }
}