import {useContext, useState} from "react";
import {AulaGetAdapter} from "../adapters/AulaGetAdapter.ts";
import {AulaGetDB, AulaGetResponse} from "../models/AulaGetDB.ts";
import {AppContext} from "../../../App.tsx";
import {EndpointEnum} from "../../../api/EndpointEnum.ts";
import apiRequest from "../../../api/apiRequest.ts";
import {AulaCreateAdapter} from "../adapters/AulaCreateAdapter.ts";
import {getQueryParamsFromObject} from "../../../utils/utils.ts";
import {RolesEnum} from "../../../api/RolesEnum.ts";

const endpoint = EndpointEnum.AULAS

export const useApiAulas = () => {
    const [isLoading, setIsLoading] = useState(false)
    const {setError, aulas: aulasAppContext, setAulas: setAulasAppContext, personalId, setMessage, allowRoles} = useContext(AppContext)

    const getAulas = async () => {
        setIsLoading(true)
        if (aulasAppContext) {
            setIsLoading(false)
        }
        let url = endpoint.toString()
        if (allowRoles!([RolesEnum.TEACHER])){
            url += "?avaliable=true"
        }
        const res = await apiRequest.getApi(url)
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
        const res = await apiRequest.postApi(endpoint, aula)
        if (!res.ok)
            setError!(new Error(res.statusText))
        await getAulas()
        setIsLoading(false)
    }
    const updateAula = async (id: string, aula: AulaCreateAdapter) => {
        setIsLoading(true)
        const res = await apiRequest.patchApi(endpoint, id, aula)
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

    const solicitarAula = async (classRoom: {classroom_id: string}) => {
        setIsLoading(true);
        const res = await apiRequest.postApi(EndpointEnum.CLASSROOM_REQUEST+"/"+personalId, classRoom);
        if (!res.ok)
            setError!(new Error(res.statusText));
        else
            setMessage!("Solicitud enviada correctamente")
        await getAulas()
        setIsLoading(false);
    };

    return {
        isLoading,
        getAulas,
        createAula,
        deleteAula,
        updateAula,
        solicitarAula
    }
}