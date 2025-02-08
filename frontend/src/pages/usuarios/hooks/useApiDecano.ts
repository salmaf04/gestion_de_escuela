import {useContext, useState} from "react";
import {AppContext} from "../../../App.tsx";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";
import {getQueryParamsFromObject} from "../../../utils/utils.ts";
import {useApiEstudiante} from "../../estudiantes/hooks/useApiEstudiante.ts";
import {ProfesorGetAdapter} from "../../profesores/adapters/ProfesorGetAdapter.ts";
import {ProfesorDB} from "../../profesores/models/ProfesorGetDB.ts";
import {ProfesorCreateAdapter} from "../../profesores/adapters/ProfesorCreateAdapter.ts";
import {getProfesorCreateDbFromAdapter} from "../../profesores/utils/utils.ts";

const endpoint = EndpointEnum.DEAN

export const useApiDecano = () => {
    const [isLoading, setIsLoading] = useState(false)
    const {setError, decanos: decanosAppContext, setDecanos: setDecanosAppContext} = useContext(AppContext)
    const [decano, setDecano] = useState<ProfesorGetAdapter>()
    const {getEstudiantes} = useApiEstudiante()

    const getDecanos = async () => {
        setIsLoading(true)
        if (decanosAppContext) {
            setIsLoading(false)
        }
        await getEstudiantes()
        const res = await apiRequest.getApi(endpoint)
        if (res.ok) {
            const data: ProfesorDB[] = await res.json()
            const decanoArray = Object.values(data)
                .map((decano: ProfesorDB) => new ProfesorGetAdapter(decano))
            setDecanosAppContext!(decanoArray)
        } else {
            setError!(new Error(res.statusText))
        }
        setIsLoading(false)
    }

    const createDecano = async (decano: ProfesorCreateAdapter) => {
        setIsLoading(true)
        const res = await apiRequest.postApi(endpoint, getProfesorCreateDbFromAdapter(decano))
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getDecanos()
        setIsLoading(false)
    }
    const updateDecano = async (id: string, decano: ProfesorCreateAdapter) => {
        setIsLoading(true)
        const res = await apiRequest.patchApi(endpoint, id, decano)
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getDecanos()
        setIsLoading(false)
    }

    const deleteDecano = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        await getDecanos()
        setIsLoading(false);
    };

    const getDecano = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.getApi(endpoint, getQueryParamsFromObject({id: id}));
        if (res.ok){
            const data: ProfesorDB[] = await res.json()
            setDecano(new ProfesorGetAdapter(data[0]))
        }
        if (!res.ok)
            setError!(new Error(res.statusText));
        await getDecanos()
        setIsLoading(false);
    };


    return {
        isLoading,
        getDecanos,
        createDecano,
        deleteDecano,
        updateDecano,
        getDecano,
        decano,
    }
}