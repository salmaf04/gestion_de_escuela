import {useContext, useState} from "react";
import {AulaGetAdapter} from "../adapters/AulaGetAdapter.ts";
import {AulaGetDB, AulaGetResponse} from "../models/AulaGetDB.ts";
import {AppContext} from "../../../App.tsx";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";
import {AulaCreateAdapter} from "../adapters/AulaCreateAdapter.ts";
import {getAulaCreateDbFromAdapter} from "../utils/utils.ts";

const endpoint = EndpointEnum.AULAS

export const useApiAulas = () => {
    const [isLoading, setIsLoading] = useState(false)
    const {setError, aulas: aulasAppContext, setAulas: setAulasAppContext} = useContext(AppContext)

    const getAulas = async () => {
        setIsLoading(true)
        if (aulasAppContext) {
            setIsLoading(false)
        }
        const res = await apiRequest.getApi(endpoint)
        if (res.ok) {
            const data: AulaGetResponse = await res.json()
            const aulaArray = Object.values(data)
                .map((aula: AulaGetDB) => new AulaGetAdapter(aula))
            setAulasAppContext!(aulaArray)
        } else {
            setError!(new Error(res.statusText))
        }

        setIsLoading(false)
    }

    const createAula = async (aula: AulaCreateAdapter) => {
        setIsLoading(true)
        const res = await apiRequest.postApi(endpoint, getAulaCreateDbFromAdapter(aula))
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getAulas()
        setIsLoading(false)
    }
    const updateAula = async (id: string, aula: AulaCreateAdapter) => {
        setIsLoading(true)
        const res = await apiRequest.patchApi(endpoint, id, getAulaCreateDbFromAdapter(aula))
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getAulas()
        setIsLoading(false)
    }

    const deleteAula = async (id: string) => {
        setIsLoading(true);
        const res = await apiRequest.deleteApi(endpoint, id);
        if (!res.ok)
            setError!(new Error(res.statusText));
        await getAulas()
        setIsLoading(false);
    };

    return {
        isLoading,
        getAulas,
        createAula,
        deleteAula,
        updateAula
    }
}